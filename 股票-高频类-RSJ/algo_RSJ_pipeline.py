# -*- coding: utf-8 -*-

import pandas as pd
import os
import dataGet_Func as dataGet
from run_func import multi_run
import importlib
import pickle
import backtest


class G:
    """
    全局对象 G，用来存储用户的全局数据
    """
    pass


# 创建全局对象g
g = G()


def initialize(context):
    """
        用户输出初始设定，在回测时只会在启动的时候触发一次
    :param context: Context对象，因子的各种属性上下文
    """
    if not os.path.exists(context.config['factor_dir'] + context.config['file_name_factor_IO']):
        # 获取源数据并筛选列名
        g.dataTrade, dataFactorSrc, g.dataBenchmark, context.fired = getattr(dataGet, "dataGet_filter")(context.config["param_dataSrc"])
        #  ——————————————————————————————以下为因子逻辑——————————————————————————————


        #  ——————————————————————————————因子信号生成（可以修改）——————————————————————————————
        # # 判断是否存在当前模型文件，或者在当前模型函文件中是否存在对应功能函数
        if not importlib.util.find_spec(context.config['model_path']+context.config['file_name_model']) \
                or not hasattr(importlib.import_module(context.config['model_path']+context.config['file_name_model']), context.config['func_name_factor']):
            context.fired = True
            print("该因子不在因子定义中！或该因子未指定功能模块文件！")
            return
        factor_module = importlib.import_module(context.config['model_path']+context.config['file_name_model'])
        if isinstance(context.config['param_factor'], dict):  # 如果参数是字典，则将股票数据和字典解包作为参数传递
            g.signals = getattr(factor_module, context.config['func_name_factor'])(dataFactorSrc, **context.config['param_factor'])
        elif isinstance(context.config['param_factor'], list):  # 如果参数是列表，则将股票数据和列表解包作为参数传递
            g.signals = getattr(factor_module, context.config['func_name_factor'])(dataFactorSrc, *context.config['param_factor'])
        else:  # 没有给出任何参数
            g.signals = getattr(factor_module, context.config['func_name_factor'])(dataFactorSrc)
        #  ——————————————————————————————因子信号生成（结束）——————————————————————————————



        #  ——————————————————————————————以下为因子交易时间范围及初始化——————————————————————————————
        # # 调用 get_trade_cal 函数生成 date_range_src ,用于交易循环遍历所依据的日期序列，源数据文件存储在 context.data_dir 路径中
        # date_range_src = dataGet.get_trade_cal(data_dir=context.data_dir)
        # # 将 date_range_src 转为只含有开盘日期的series
        # date_range_src = pd.Series(date_range_src[(date_range_src['is_open'] == 1)]['cal_date'].values)
        # # 如果需要修改 date_range_src 的原始时间序列内容，需在该注释下修改，将修改后的时间序列再对context对应属性进行初始化；
        date_range_src = pd.to_datetime(pd.Series(g.dataTrade.index).drop_duplicates().sort_values())    # 使用现有数据构造date_range样例；

        # 用 date_range_src 补齐 g.dataTrade的索引日期（索引日期必须是datetime.datetime时间戳格式）;
        g.dataTrade = pd.DataFrame(index=date_range_src).combine_first(g.dataTrade)
        # 用 date_range_src 补齐 g.signals的索引日期（索引日期必须是datetime.datetime时间戳格式）;combine_first要求g.signals为DataFrame；
        g.signals = pd.DataFrame(index=date_range_src).combine_first(pd.DataFrame(g.signals))
        # 用 date_range_src 补齐g.dataBenchmark的索引日期（索引日期必须是datetime.datetime时间戳格式）;
        g.dataBenchmark = pd.DataFrame(index=date_range_src).combine_first(g.dataBenchmark) if not pd.DataFrame(g.dataBenchmark).empty else None

        # 将g.dataTrade, g.signals, date_range_src存入字典保存到dataSrc_path
        with open(context.config['factor_dir'] + context.config['file_name_factor_IO'], "wb") as f:
            pickle.dump({'dataTrade': g.dataTrade, 'signals': g.signals, 'dataBenchmark': g.dataBenchmark, 'date_range_src': date_range_src}, f)

    else:
        # 直接读取已经生成的因子文件并获取各变量数据
        with open(context.config['factor_dir'] + context.config['file_name_factor_IO'], 'rb') as f:
            dataSrc_dict = pickle.load(f)
        # 按键名获取数据
        g.dataTrade, g.signals, g.dataBenchmark, date_range_src = dataSrc_dict['dataTrade'], dataSrc_dict['signals'], dataSrc_dict['dataBenchmark'], dataSrc_dict['date_range_src']

    # 将context相应的属性初始化；date_range_src 日期格式化之后赋值给 context.date_range，根据context.start_date和context.end_date截取并修改context.date_range；
    backtest.init_trade_cal(context=context, date_range=date_range_src, globals=globals())


def handle_data(context):
    """
        因子具体逻辑实现的函数，每个时刻只被调用一次，在此函数进行下单
    :param context: Context对象，因子的各种属性上下文
    """
    # 获取当前时间、当前标的价格数据
    price = g.dataTrade.loc[context.current_dt, 'close']    # 如果是多标的，不能直接获取价格，需要先筛选标的！！！
    # 读取当天交易信号
    signal = g.signals.loc[context.current_dt].values[0]
    # 仅在第一天执行
    if context.current_dt == context.date_range[0]:
        # 子账户3：全仓持有标的
        backtest.order_target_percent(context, context.security, price, 1, 3)
    # 如果rsj值小于0
    if signal < 0:
        # 如果股票不在子账户1的持仓中，全仓买入
        if context.security not in context.portfolios[1].positions:
            backtest.order_target_percent(context, context.security, price, 1, 1)
        # 如果股票在子账户2的持仓中，清仓
        if context.security in context.portfolios[2].positions:
            backtest.order_target_percent(context, context.security, price, 0, 2)
    # 如果rsj值大于0
    if signal > 0:
        # 如果股票在子账户1的持仓中，清仓
        if context.security in context.portfolios[1].positions:
            backtest.order_target_percent(context, context.security, price, 0, 1)
        # 如果股票不在子账户2的持仓中，全仓买入
        if context.security not in context.portfolios[2].positions:
            backtest.order_target_percent(context, context.security, price, 1, 2)


def update_value(context, afterTrading=False):
    """
        更新每个portfolio和benchmark的价格和价值，盘前和盘后分别更新一次
    :param context: Context对象，因子的各种属性上下文
    :param afterTrading: bool, 是否是盘后更新，默认为否
    """
    # 遍历每个子账户
    for i in range(context.subportfolio_num + 1):
        # 遍历子账户中的持仓标的
        for stock in context.portfolios[i].positions_all:
            # 读取当前价格数据
            # price = g.dataTrade.loc[(g.dataTrade.index == context.current_dt) & (g.dataTrade['ts_code'] == stock), 'close'].values[0]
            # price = g.dataTrade[g.dataTrade['ts_code'] == stock].loc[context.current_dt, 'close']
            price = g.dataTrade.loc[context.current_dt, 'close']    # 如果是多标的，不能获取价格，需要先筛选标的！！！
            # 将所有指标存储为字典, 止损指标数据调用stopLoss
            attributes = {**{"price": price}}
            # 更新持仓标的的指标
            context.portfolios[i].positions_all[stock].update(current_dt=context.current_dt, attributes=attributes, afterTrading=afterTrading)
    for key in context.benchmark.keys() if context.benchmark else []:
        # 存储benchmark每个组成部分的价格
        context.benchmark_return.loc[context.current_dt, key] = g.dataBenchmark.loc[context.current_dt, key] if not pd.DataFrame(g.dataBenchmark).empty else 0
    # 更新context
    context.update(afterTrading=afterTrading)


def before_trading(context):
    """
        盘前处理函数，每天策略开始交易前会被调用，不能在这个函数中发送订单
    :param context: Context对象，因子的各种属性上下文
    """
    # 调用更新函数更新价值和价格
    update_value(context=context, afterTrading=False)


def after_trading(context):
    """
        盘后处理函数，每天收盘后会被调用，不能在这个函数中发送订单
    :param context: Context对象，因子的各种属性上下文
    """
    # 调用更新函数更新价值和价格
    update_value(context=context, afterTrading=True)



if __name__ == "__main__":
    import config_super  # 导入全局配置
    import config as config_local

    # 用传入的远端config_super中的CONFIG更新本地CONFIG
    CONF_merge = config_super.update_config(super_config=config_super.CONFIG, config_local=config_local.CONFIG_factor)
    # 生成配置组合
    configs = config_super.generate_config_combinations(CONF_merge)  # [0:2]

    result_output, multi_run_result = multi_run(config_super.CONFIG, configs, initialize, before_trading, handle_data, after_trading)
    # result_output, multi_run_result = multi_run(super_config=config_super.CONFIG, config_local=configs, initialize=initialize, before_trading=before_trading, handle_data=handle_data, after_trading=after_trading)
    # result_output, multi_run_result = multi_run(super_config=config_super.CONFIG, config_local=configs)
    # result_output, multi_run_result = multi_run(super_config={}, config_local=configs)
    # result_output, multi_run_result = multi_run({}, configs, initialize, before_trading, handle_data, after_trading)

    result_output.to_pickle('result/result.pkl')
    import pickle
    pickle.dump(multi_run_result, open("result/all_result.pkl", "wb"))

    print("done")
