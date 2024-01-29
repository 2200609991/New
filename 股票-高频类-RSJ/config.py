# -*- coding: utf-8 -*-
# coding=utf-8
# 主要功能：本地config设置


# 本地总CONFIG
CONFIG = {
    # # ——————————全局配置项，整体策略（非各个子账号）统一配置项：——————————
    # 全局配置说明：配置项对所有子账户、所有账户类型、所有标的同时有效；不能单独指定某个单独子账户、单独账户类型、单独标的进行特定设置；
    # 动态修改方法：可以在factor_dict中重新赋值；也可以使用set_option_global(context, configs)修改；
    # 配置方法适用配置项：适用于当前位置到"分账户编号控制配置"前所有配置项；

    # 因子路径，因子所在文件夹名称；
    "factor_path": [""],
    # 因子中文名称；如果为空，会用"func_name_factor"的非空值填充；
    "factor_name": [""],
    
    # 因子英文名称
    "factor_name_EN": [""],
    # 创建人
    "creator": [""],
    # 因子ID;分配给因子的唯一标识符或ID
    "factor_id": [""],
    # 因子分类;描述因子属于哪个类别或类型
    "factor_category": [""],
    # 因子方向;指定因子的预期方向（如正向、负向）
    "factor_direction": [""],
    # 行业分组（按行业分组，或否）;指定是否按行业进行分组;
    "industry_grouping": [""],
    # 行业分类（申万一级行业、中信一级行业、证监会行业分类等）;指定使用哪种行业分类标准
    "industry_classification": [""],
    # 行业权重（行业中性、市值加权、流通市值加权等）;指定行业权重的计算方法
    "industry_weighting": [""],
    # 个股权重（等权重等）
    "stock_weighting": [""],  # 指定个股权重的计算方法
    # 极值处理（中位数法等）;指定处理极值的方法
    "extreme_value_processing": [""],
    # 无量纲化（即标准化：z值法）;指定数据标准化的方法
    "dimensionless_processing": [""],
    # 证券名称缩写，在中国A股是股票拼音缩写，如：'PAYH'是平安银行证券名缩写；期货市场中如'HS1005'，主力连续合约与指数连续合约都为'null'。
    "abbrev_symbol": [""],

    # 配置编号
    "config_index": [],
    # all_factor层是否并行，只在all_factor_Demo使用，pipeline、backtest中不使用；
    "multiProcess_all_factor": [False],
    # multi_run层是否并行
    "multiProcess_multiRun": [True],   # False
    # 是否进行性能分析：
    "enable_profiler": [False],     # True   False
    # 系统日志级别，用于控制策略框架输出日志的详细程度（策略打印的日志不受该选项控制），设置为某一级别则框架会输出该级别及更"严重"的日志
    # 可选值："debug"|"info"|"warning"|"error"，通常推荐设置为 info 或 warning
    "log_level": ["info"],
    # 数据存放路径
    "data_dir": ["data/"],
    # 结果输出路径
    "output_dir": ["result/"],
    # 因子值、交易数据、交易日期等结果输出路径
    "factor_dir": ["factor/"],
    # 回测开始日期；支持'年-月-日'['2018-11-23']、'年-月-日 时:分:秒'['2018-11-23 11:12:13']、'年-月-日 时:分:秒.毫秒'['2018-11-23 11:12:13.12345']格式;
    "start_date": ['2018-11-22 11:12:13.12345'],
    # # 向前获取几个交易频点，根据end_date和dt_count来反算start_date，dt_count的数量是基于date_range来计数；dt_count与start_date二选一，不可同时使用。
    "dt_count": [],
    # 回测结束日期；支持'年-月-日'['2018-11-23']、'年-月-日 时:分:秒'['2018-11-23 11:12:13']、'年-月-日 时:分:秒.毫秒'['2018-11-23 11:12:13.12345']格式;
    "end_date": ['2019-01-02'],     # , '2021-05-25'    2018-12-31
    # 一年包含的数据条数（一个周期内含有的日期数量）；如日频数据中，自然日365，工作日252，周度52，月度12，季度4，半年度2；
    "period": [252],
    # 子账户数（即分组测试的分组数量）
    "subportfolio_num": [3],
    # 是否设置多空子账户（多空分组）：[]中值为所在子账户的subportfolio_index（即分组的编号）；如果不设置，则值为None。
    "long": [1],  # 多头，值为对应子账号（分组）编号
    "short": [2],  # 空头，值为对应子账号（分组）编号
    # 回测基准，字典
    "benchmark": [],  # {"000300.XSHG": 1}    {"000300.XSHG": 0.7, "110044.XSHG": 0.3}
    # 是否允许小数下单
    "decimal_order": [True],
    # 是否启用强行平仓
    "forced_liquidation": [False],
    # 记录的属性；可选值："value", "price", "trade","factor_value", "capacity", "maxLoss_ratio", "maxLoss_stastic", "max_loss_MDD", "volatilityMultiple_MA", "volatilityMultiple_STD"
    # 除 "value", "trade"外，其它值均需在update_value()中将对应值以键值对形式赋值给attributes；
    "attributes": [["value", "price", "trade"]],
    # 衍生表是否开启：时间为键；
    "attributes_time_df": [True],
    # 衍生表是否开启：证券标的名称为键；
    "attributes_security_df": [True],
    # IC生成类型，一个列表，可以为空；pipeline中使用；
    # 可选值：["IC_all_crossSection", "IC_subportfolio_crossSection", "IC_subportfolio_retRatio"]
    "IC_types": [["IC_all_crossSection", "IC_subportfolio_crossSection", "IC_subportfolio_retRatio"]],
    # IC滞后值，可以是list或者int，也可以置空；pipeline中使用；
    "IC_lag_n": [[1, 2]],    # [1,2,3]
    # 是否在run()层输出结果     # ys:暂未使用，run()层结果直接返回到 multi_run 层进行合并了。
    "output_run": [True],
    # 是否输出运行时间表     # ys:暂未使用，默认直接输出。
    "timing": [True],
    # 是否允许交易中出现停牌    # ys：暂未使用；如果price为0，则认为是停牌，会输出log，并不会终止执行；
    "suspension": [True],
    # 基金申购份额到账天数    # ys:暂未使用；
    "subscription_receiving_days": [1],
    # 基金赎回款到账天数    # ys:暂未使用；
    "redemption_receiving_days": [1],
    # 基金前端费率    # ys:暂未使用；
    "fee_ratio": [0],
    # 融资利率/年    # ys:暂未使用；
    "financing_rate": [0],
    

    
    # # ——————————全局回测频率控制：——————————
    # 全局回测频率控制通用说明；为0、为空表示不控制频率；可选值：minutely、daily、weekly、monthly、quantly、half_yearly、yearly、正整数值间隔；
    # 配置方法适用配置项："frequency"、"SELECT_INTERVAL"、"BUY_INTERVAL"、"SELL_INTERVAL"
    # 动态修改方法：可以在factor_dict中重新赋值；也可以使用set_option_global(context, configs)修改；

    # 回测周期；为0、为空表示不控制频率；
    "frequency": [],    # 1 "daily"
    # 调仓周期（每多少个交易日更新一次股票池）；这个跟daily等交易频率互斥；
    "SELECT_INTERVAL": [],    # 1 "daily"
    # 买入周期（每多少个交易日执行一次买入操作）；为0、为空表示不控制频率；
    "BUY_INTERVAL": [],    # 1 "daily"
    # 卖出周期（每多少个交易日执行一次卖出操作）；默认与买入周期相同；为0、为空表示不控制频率；
    "SELL_INTERVAL": [],    # 1 "daily"


    # # ——————————分账户编号控制配置：——————————
    # 分账户编号控制配置通用说明：按照账户数字编号配置;(1)只有单值，表示对所有账户类型、所有标的都按照该值进行设定；(2)按照编号指定配置；范例如下：
    # # 具体子账户数量可以根据代码对应修改；分子账户指定，账户数量与之前的"subportfolio_num"一致；账户0默认不限制，也不出现在这里。其它账户如果没有出现，就表示不限制；
    # # 为0、为空、为None、为1，这些值既可以在"subportfolio_num"的键后面作为值，也可以直接放在[]内，不带键；如果为0、为空、为None就不判断，
    # # 如："MAX_HOLDING_NUM": [{1: 0/(空)/None/1, 2: 0/(空)/None/1, 3: 0/(空)/None/1}],
    # # 或者："MAX_HOLDING_NUM": [1: 0/(空)/None/1],    # 相当于对所有账户进行全体控制了。
    # 配置方法适用配置项："account_type"、"cash"、"MAX_HOLDING_NUM"、"MAX_WEIGHT"
    # 动态修改方法：可以在factor_dict中重新赋值；也可以使用set_subportfolios(context, subportfolio_conditions, subportfolio_index=None)修改；

    # 账户类型DEFAULT_ACCOUNT_TYPE；不同的Portfolio可以不同的type，如果为空，默认为stock；如果只给一个值，则全部Portfolio都是该值类型。或者字典。可选类型如下：
    # 股票类（权益类,stock_set）:股票'stock'、index(指数);
    # 期货类（future_set）: 期货 'futures'、金融期货(股指期货)'index_futures'、商品期货'commodity_futures'、国债期货'government_futures';
    # 期权类（option_set）: 期权'options'、商品期权'commodity_option'、股指期权'index_option'、ETF期权'ETF_option';
    # 基金类（fund_set）: 场内ETF基金(交易型开放式指数基金)'etf'、场内基金 'fund'、债券基金'bond_fund'、股票基金'stock_fund'、QDII基金'QDII_fund'、混合基金‘mixture_fund'、货币基金'money_market_fund'、
    #     场外基金（开放式基金）'open_fund'、lof（上市型开放基金）、fund_fund（联接基金)、场内交易的货币基金 'mmf' 、
    #     分级A基金（场内分级A）'fja'、分级B基金（场内分级B）'fjb'、分级母基金（场内分级母基金）'fjm'
    # 债券类（bond_set）: 债券(bond)、可转债（convertible_bond）;
    # 外汇类（foreign_exchange_set）: 外汇（foreign_exchange）（包括货币、汇率等方面）;
    # 另类资产类（alternative_asset_set）: 另类资产（alternative_asset）（包括非标产品、虚拟货币等）;
    # 账户类型；支持全局统一值设置（单值）、不同子账户编号设置;
    "account_type": ["stock"],  # "stock"    {1: "stock", 2: "fund", 3: "options"}
    # 初始现金；支持全局统一值设置（单值，等权分配）、不同子账户编号设置;
    "cash": [300000000],        # "cash": [300000000] 、"cash": [{1: 10000, 2: 5000, 3: 15000}]
    # 最大持仓股票数（策略最多持有的标的数量），超过了不能再买入，不限制总账户、多空账户和基准账户;支持全局统一值设置（单值）、不同子账户编号设置;
    "MAX_HOLDING_NUM": [],
    # 个股最大持仓比重（策略每个标的的最大比例）；支持全局统一值设置（单值）、不同子账户编号设置;(未完全启用！！！)
    "MAX_WEIGHT": [],
    
    
    # # ————————全体配置、按账户类型配置、按每个标的配置:存储在“context.instrument”表中；——————————
    # 配置通用说明：(1)如果给单值，未按照账户类型设置，则表示所有账户类型都使用该统一值；(2)按照账户类型或单个标的配置；范例如下：
    # # 全体统一值配置: "margin_rate": [1],    # 只有单值，表示对所有账户类型、所有标的都按照该值进行设定；该值存储在“Instrument”表中"default"行；
    # # 按账户类型配置: "margin_rate": [{"stock": 1, "future": 1, "fund": 0.003}],    # 按账户类型设置，表示该类型账户下都是该值；存储在“Instrument”表中；
    # # 按每个标的配置: "margin_rate": [{"000001.XSHE": 1, "000002.XSHE": 0.8, "IF": 0.0003}],    # 按单独标的设置，存储在“Instrument”表中；
    # # 账户类型与标的混合设置："round_lot": [{"stock": 100, "000002.XSHE": 0.8, "IF": 0.0003}],     # 按账户类型和标的混合设置，存储在“Instrument”表中；
    # 配置方法适用配置项："round_lot"、"contract_multiplier"、"maturity_date"、"margin_rate"、"margin_multiplier"、"open_tax"、"close_tax"、"open_commission"、
    # # "close_commission"、"min_commission"、"commission_multiplier"、"fixed_slippage"、"price_related_slippage"、"management_fee_rate"、"locked_period"
    # 动态修改方法：可以在factor_dict中重新赋值；也可以使用set_option_instrument(context, conditions, ref=None)修改；

    # 交易最低限额乘数；【int】股票：一手对应多少股，中国A股一手是100股。期货：一律为1。支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "round_lot": [1],  # 1    100     {"stock": 100, "fund": 1, "future": 1}
    # 【float】合约乘数；其中股票、基金为1，期货为相应的合约乘数；对price的放大；与price几乎同步出现。例如沪深300股指期货的乘数为300.0（期货专用）；支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "contract_multiplier": [1],    # 样例： 1  300 {"000001.XSHE": 1, "000002.XSHE": 100, "IF": 1000}
    # 【str】到期日（期货等）。主力连续合约与指数连续合约都为空; 会触发该标的的强平；需要在因子内自行调用、判断和触发相关操作；支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "maturity_date": [],     # 样例：{"000001.XSHE": 'XXXX-XX-XX', "000002.XSHE": '2023-11-01'}
    # 保证金率，每个标的可能是不同的，每个标的默认为1，股票为0; 支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "margin_rate": [1],    # 样例：{"stock": 0.9, "000002.XSHE": 0.8, "IF": 0.0003}
    # 保证金倍率，券商增加的，每个账户类别默认为1；支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "margin_multiplier": [1],    # 样例：{"stock": 1, "IF": 1000, "future": 1.1}
    # 买入印花税率; 支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "open_tax": [0],  # 0, 0.001, 0.002    # 样例：{"stock": 0, "000001.XSHE": 0.001, "future": 0.0003}
    # 卖出印花税率; 支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "close_tax": [0],  # 0, 0.001, 0.002    # 样例：{"stock": 0, "000001.XSHE": 0.001, "future": 0.0003}
    # 买入手续费率；佣金费率；基金是申购费率；支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "open_commission": [0],    # 0, 0.0001, 0.0003    # 样例：{"stock": 0, "000001.XSHE": 0.001, "future": 0.0003}
    # 卖出手续费率；佣金费率；基金是赎回费率；支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "close_commission": [0],    # 0, 0.0001, 0.0003    # 样例：{"stock": 0, "000001.XSHE": 0.001, "future": 0.0003}
    # 最小手续费; 支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "min_commission": [0],  # 0, 5    # 样例：{"stock": 0, "000001.XSHE": 1, "future": 2}
    # 佣金倍率，券商增加的，每个账户类别默认为1；支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "commission_multiplier": [1],    # 样例：{"stock": 0, "000001.XSHE": 0.001, "future": 0.0003}
    # 固定值滑点; 支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "fixed_slippage": [0],  # 0, 0.01, 0.02    # 样例：{"stock": 0, "000001.XSHE": 0.001, "future": 0.0003}
    # 百分比滑点; 支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "price_related_slippage": [0],  # 0, 0.002    # 样例：{"stock": 0, "000001.XSHE": 0.001, "future": 0.0003}
    # 管理费率；管理费 = total_value * 管理费率（除以365后折算到每日的费率）,每日计提；不含超额计提，超额计提需在指定日期计提并单独计算。支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "management_fee_rate": [0],   # 样例：{"stock": 0.0001, "000001.XSHE": 0.0001, "future": 0.0002}
    # 冻结期；如股票T+0、T+1限制，期货T+0，基金申赎的T+1、T+2、T+3等；支持全局统一值设置（单值）、不同账户类型、标的混合设置;
    "locked_period": [{"stock": 0}]    # 样例：{"stock": 1}    {"stock": 1, "000001.XSHE": 2, "future": 3}
}


field_mapping_table = {
    # # ——————————字段映射表：——————————
    # 跨数据库、跨表、跨品种字段名称映射
    # 此处汇总不同数据库、不同数据表、不同品种的相同字段的映射关系；
    # 键值对是源数据字段命名规则与因子需要不同，需要重命名；

    "colName_field_mapping": [{
        # 自定义字段映射：

        # Tushare数据库：
        # Tushare 通用字段映射：
        'trade_date': 'date',
        # 基金
        # 'unit_net_value': 'close',
        'adj_nav': 'close',
        'nav_date': 'date',

        # 某数据库：
        # 某张数据表：字段映射：

    }]
}


config_custom = {
    # # ——————————自定义配置项：——————————
    # 自定义配置项说明：因子自有配置项，只能在因子空间主动使用，不进backtest，不一定出现在远端config中。
    # 动态修改方法：可以在factor_dict中重新赋值；也可以set_option_instrument(context, conditions, ref=None)修改；

    "name": ["刘雨秋"],
    "ID": ["420683199909180035"],
    "Tel": ["13098455337"],
    "mail": ["2200609991@qq.com"],
    "organazation": ["中央财经大学"],


    # 筛选项：过滤市值
    "filter_market_value": [],
    # 筛选项：过滤停牌
    "filter_suspension": [],
    # 筛选项：基金筛选
    "filter_fund_xxx": [],

    # 策略中用于交易证券标的；当交易交易与信号生成的证券标的相同是，则两者全部保存在此变量。也可以不使用该变量，自行定义变量名称来存储交易证券标的；
    # 如果为股票列表，需存放在config_universe，使用universe系列配置项调用；该配置项内容不能过多，否则影响因子文件名称生成；
    "security": ['002267.XSHE'],  # '000300.XSHG', '002267.XSHE', '002268.XSHE'
    # 策略中用于交易证券标的生成；如果信号生成与交易部分标的不一样时，单独存储交易生成证券标的时所需股票；
    "security_trade": [],  #
    # 策略中用于信号生成的证券标的；如果信号生成与交易部分标的不一样时，单独存储信号生成证券标的时所需股票；
    "security_signal": [],  #
    # 通用股票池，同时用于信号和交易；会提取并合并到security中；限单值，不支持list;rqalpha命名法，rqalpha中用于订阅标的的范围，也是交易标的的范围；
    "universe": [],  # "config_universe.HS300_2009"
    # 股票池，用于交易标的生成；限单值，不支持list;
    "universe_trade": [],  # "config_universe.HS300_2009"
    # 股票池，用于信号生成；限单值，不支持list;
    "universe_signal": [],  # "config_universe.HS300_2009"
    # todo：考虑除security、universe外，其它字段是否有必要区分trade和signal，或使用{"trade":"对应变量单值/多值"}？？？

    # 策略用到的参数m：
    "m": [13],
    # 窗长
    "window": [10],
    # 因子函数名称；可能与factor_name不止相差"_signal"，如信号为多个因子组合生成时；
    "func_name_factor": [],
    # 源数据获取函数名称
    "func_name_dataSrc": [],
    # 因子参数
    "param_factor": [],
    # 源数据参数，保存读取源数据的字典集；该字段内包含的参数将送入数据获取函数进行源数据的各种处理；
    # 已默认添加配置项，会将对应的原始键值对（无论是factor_dict还是CONFIG中）在因子无指定时赋值到该“源数据参数”中；
    # 默认添加配置项如下：["data_dir", "benchmark", "universe", "universe_trade", "universe_signal", "security", "security_trade", "security_signal",
    #   "strategy_type", "colName_dataSrc", "colName_derived_ref", "file_name_dataSrc", "func_name_dataSrc", "data_usage_purpose", "file_name_factor_IO", "colName_field_mapping"]
    # todo：需要测试该字段是否需要支持list中带多组集合的情形，即完整取数的参数组合，是否有足够多应用场景？？？如果需要，则需要将该配置项合并？还是覆盖到"factor_dict"中对应字段？
    "param_dataSrc": [],

    # # "colName_dataSrc" 和 "colName_derived"共同构成用于因子源数据输入字段；为源数据必须直接包含的因子需要的字段；如果没有因子所需要的字段，则不启动计算该因子。
    # # # 如果此处和factor_dict中都为空，表示不限制输入字段数量，如机器学习中，输入特征数量可以不限制；
    # 因子需要的源数据的列名、数据字段，即可以从源数据库中直接获取到的字段；
    # 只支持单值或单值构成的列表！！！不支持键对值！！！
    "colName_dataSrc": [],  # ['open', 'trade_date', 'unit_net_value']
    # 因子需要的衍生指标的列名、数据字段，即源数据库中没有该字段，需自行计算并生成的衍生指标。
    "colName_derived": [],  # ['ret']
    # 因子衍生指标计算需要参考的列,对该列进行各种衍生指标的计算和变形；
    "colName_derived_ref": [],  # ['close']，用于生成衍生字段['ret']时使用；
    # 数据用途：用于交易、生成信号；默认为空，为同时用于生成信号和交易；可选项：'trade', 'signal', []空值；
    "data_usage_purpose": [],
    # 策略类型
    "strategy_type": [],   # "日频"  "日内高频"
    # 策略方法类型;可选值:"择时"、"选股"、"资产配置"、"机器学习和深度学习"
    "strategy_method_type": [],
    # 策略类型；可选值："技术指标"、"动量"、"反转"、"配对交易"、"高频投资"、"算法交易"、"套利"等；、
    "strategy_indicators_type": [],
    # 源数据文件名称
    "file_name": [],
    # 源数据文件名称
    "file_name_dataSrc": [],
    # 输入和输出的因子文件名称；命名规则为"func_name_factor"__"universe"__"security",存储在"factor_dir"中;
    "file_name_factor_IO": [],
    # 模型路径，模型算法文件所在文件夹名称；用于机器学习等抽取出来的统一模型文件存放的路径；作为import时的路径；
    "model_path": [""],
    # 模型文件名称，模型文件名称要使用模型本身名称来直接命名；作为import引入时使用,不带后缀；如果有相对路径，需要加上；
    # 如因子存放在"factor_RSJ.py"中，则需要import该模型文件，
    "file_name_model": ["factor_RSJ"],

    # 因子字典集；
    # # # 每个因子必须给出的参数如下（其它参数可自行增减）：
    # # "factor_dict": [{"func_name_factor": "因子名称、因子名称_signal", # 此处必须有
    # #                  "param_dataSrc": {"func_name_dataSrc": "read_file",    # 必须有；通用配置和此处设置，两种可都有，或至少选其一；
    # #                                    "colName_dataSrc": ['trade_date', 'close', 'ret']},  # 必须有；通用配置和此处设置，两种可都有，或至少选其一；必须是单值或单值构成的list，不能有键值对！！！
    # #                  "param_factor": {"参数1": "参数值", "参数2": "参数值"},  # 非必须；根据因子需要可选；
    # #                  "file_name_model": ["factor_RSJ"],  # 必须有；通用配置和此处设置，两种可都有，或至少选其一；
    # #                  # 说明：在"param_dataSrc"外部的配置项，除规定的排除项外，也会默认添加到"param_dataSrc"的list中的每个集合内，并传入dataGet中供调用；
    # #                  # # 如果想让"param_dataSrc"的list中的每个字典有特有配置项，，则需要单独在该集合中单独添加或指定；
    # #                  }],
    "factor_dict": [{"func_name_factor": "rsj",
                     # "param_dataSrc":{"func_name_dataSrc": "read_file", "colName_dataSrc": ['date', 'ret'], "file_name": "hs300.csv", "security": '002230.XSHE'},  # "security": ['002230.XSHE', '002235.XSHE']
                     # "param_dataSrc":[{"func_name_dataSrc": "read_file", "colName_dataSrc": ['date', 'ret'], "file_name_dataSrc": "hs300.csv", "security": '002230.XSHE', "data_usage_purpose":'trade'}],  # "security": ['002230.XSHE', '002235.XSHE']
                     # "param_dataSrc":[{"func_name_dataSrc": "read_file", "colName_dataSrc": ['date', 'ret'], "file_name": "hs300.csv", "security": '002230.XSHE', "data_usage_purpose":'trade'}],  # "security": ['002230.XSHE', '002235.XSHE']
                     # "param_dataSrc":[{"func_name_dataSrc": "attribute_datarange_history", "colName_dataSrc": ['ts_code', 'trade_date', 'ret', 'close'], "security": '000300.XSHG', "data_usage_purpose":'trade'},
                     #                  {"func_name_dataSrc": "read_file", "colName_dataSrc": ['ts_code', 'date', 'ret'], "file_name": "hs300.csv","file_name": "hs300.csv", "security": '002230.XSHG', "data_usage_purpose":'trade'},
                     #                  {"func_name_dataSrc": "read_file", "colName_dataSrc": ['ts_code', 'date', 'ret', 'close'], "file_name": "hs300.csv","file_name": "hs300.csv", "security": '000300.XSHG', "data_usage_purpose":'signal'}],  # "security": ['002230.XSHE', '002235.XSHE']

                     # # 期货
                     # "param_dataSrc":[{"func_name_dataSrc": "read_file", "colName_dataSrc": ['ts_code', 'date', 'close'], "file_name": "IF.csv", "security": 'IF.CFX', "data_usage_purpose":'trade'},
                     #                  {"func_name_dataSrc": "read_file", "colName_dataSrc": ['date', 'ret'], "file_name": "hs300.csv", "security": '000300.XSHG', "data_usage_purpose":'signal'}],  # "security": ['002230.XSHE', '002235.XSHE']

                     # # 期权
                     # "param_dataSrc":[{"func_name_dataSrc": "read_file", "colName_dataSrc": ['ts_code', 'date', 'close'], "file_name": "IO2104-P-4450.CFX.csv", "security": 'IO2104-P-4450.CFX', "data_usage_purpose":'trade'},
                     #                  {"func_name_dataSrc": "read_file", "colName_dataSrc": ['date', 'ret'], "file_name": "hs300.csv", "security": '000300.XSHG', "data_usage_purpose":'signal'}],  # "security": ['002230.XSHE', '002235.XSHE']
                     # "start_date": '2021-03-11',
                     # "end_date": '2021-04-13',

                     # # 基金
                     # "param_dataSrc":[{"func_name_dataSrc": "read_file", "colName_dataSrc": ['ts_code', 'date', 'close'], "file_name": "161130.SZ.csv", "security": '161130.SZ', "data_usage_purpose":'trade'},
                     #                  {"func_name_dataSrc": "read_file", "colName_dataSrc": ['date', 'ret'], "file_name": "hs300.csv", "security": '000300.XSHG', "data_usage_purpose":'signal'}],  # "security": ['002230.XSHE', '002235.XSHE']

                     # # 可转债
                     # "param_dataSrc":[{"func_name_dataSrc": "read_file", "colName_dataSrc": ['ts_code', 'date', 'close'], "file_name": "128024.SZ.csv", "security": '128024.SZ', "data_usage_purpose":'trade'},
                     #                  {"func_name_dataSrc": "read_file", "colName_dataSrc": ['date', 'ret'], "file_name": "hs300.csv", "security": '000300.XSHG', "data_usage_purpose":'signal'}],  # "security": ['002230.XSHE', '002235.XSHE']

                     # 股票
                     "param_dataSrc":[{"func_name_dataSrc": "attribute_datarange_history", "colName_dataSrc": ['ts_code', 'date', 'ret', 'close'], "security": '000300.XSHG', "data_usage_purpose":'trade'},
                                      {"func_name_dataSrc": "read_file", "colName_dataSrc": ['date', 'ret'], "file_name": "hs300.csv", "security": '000300.XSHG', "data_usage_purpose":'signal'}],  # "security": ['002230.XSHE', '002235.XSHE']


                     "param_factor": {"strategy_type": "日频", "m": 13},
                     "file_name_model": "factor_RSJ",
                     "factor_name":"rsj",    # 'date', 'ret'
                     "account_type": "stock", "cash": 300000000,
                     "MAX_HOLDING_NUM":0, "MAX_WEIGHT": 0,
                     "benchmark": {"000300.XSHG": 0.7, "110044.XSHG": 0.3},
                     "frequency": 1, "SELECT_INTERVAL":1, "BUY_INTERVAL":1, "SELL_INTERVAL":1,
                     "round_lot": 1,"contract_multiplier": 1, "maturity_date": None, "margin_rate": 1,
                     "margin_multiplier": 0, "open_tax": 0, "close_tax": 0, "open_commission": 0, "close_commission": 0,
                     "min_commission": 0,"commission_multiplier": 0,"fixed_slippage": 0, "price_related_slippage": 0,
                     "management_fee_rate": 0,"locked_period": {"stock": 0}
                     },
                    # {"func_name_factor": "rsj",
                    #  "param_dataSrc":{"func_name_dataSrc":"read_file", "colName_dataSrc": ['date', 'close'], "file_name": "hs300.csv"},
                    #  "param_factor": {"strategy_type": "日频", "m": 13},
                    #  "factor_name":"rsj", "colName_dataSrc": ['date', 'ret'],    # 'date', 'ret'
                    #  "account_type": {1: "stock", 2: "fund", 3: "options"}, "cash": {1: 100000000, 2: 50000000, 3: 150000000},
                    #  "MAX_HOLDING_NUM": {1: 10, 2: 20, 3: 10}, "MAX_WEIGHT": {1: 1, 2: 1, 3: 1},
                    #  "benchmark": {"000300.XSHG": 0.7, "110044.XSHG": 0.3},
                    #  # "frequency": "daily", "SELECT_INTERVAL":"weekly", "BUY_INTERVAL":4, "SELL_INTERVAL":2,
                    #  "frequency": 1, "SELECT_INTERVAL":1, "BUY_INTERVAL":1, "SELL_INTERVAL":1,
                    #  "round_lot": 100,"contract_multiplier": 300, "maturity_date": None, "margin_rate": 0.05,
                    #  "margin_multiplier": 1.2, "open_tax": 0.001, "close_tax": 0.002, "open_commission": 0.01, "close_commission": 0.1,
                    #  "min_commission": 5,"commission_multiplier": 1.1,"fixed_slippage": 0.02, "price_related_slippage": 0.002,
                    #  "management_fee_rate": 0.0001,"locked_period": {'002267.XSHE': 3,"stock": 2, "fund": 2, "options": 2}
                    #  },
                    # {"func_name_factor": "rsj",
                    #  "param_dataSrc":{"func_name_dataSrc":"read_file", "colName_dataSrc": ['date', 'close'], "file_name": '002267_SZ.pickle'},
                    #  "param_factor": {"strategy_type": "日内高频", "m": 4},
                    #  # "data_dir": "data_HF/",
                    #  "start_date": '2022-12-01', "end_date": '2022-12-20',
                    #  "benchmark": {'000001.XSHE': 1}, "period": 1452,
                    #  "factor_name":"rsj_HF", "colName_dataSrc": ['date', 'ret'],
                    #  "frequency": 1, "SELECT_INTERVAL":1, "BUY_INTERVAL":1, "SELL_INTERVAL":1
                    # }
                    ],

}

CONFIG_factor = {**CONFIG, **config_custom, **field_mapping_table}


import config_super
# 生成本地CONFIG的configs列表
configs = config_super.generate_config_combinations(CONFIG_factor)

