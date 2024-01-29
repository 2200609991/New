import pandas as pd
# df=df[df['ts_code']=='000300.XSHG']
# df = df.drop(columns=['ts_code', 'close111'])

def rsj(df, m, strategy_type="日频"):
    """
        使用5分钟级别的K线来计算RSJ指标；
        在每日的14:55计算前一段时间（可调参数）的RSJ指标；
        若RSJ指标大于0则发出空头信号，反之则发出多头信号；
        基于指标发出的交易信号，在收盘前完成交易（比如14:56）；
        持仓到第二天的14:55分，然后重复2-4步骤调整仓位。
    :param df, Series: 计算的原始数据,索引需要是日期；
    :param m, int: 窗长；
    :return: rsj, Series: 基于rsj计算得到的交易信号；
    """
    df = df.set_index('date') if 'date' in df.columns else df
    if strategy_type == "日内高频":     # 此处为日内每小时区间内的高频信号生成
        # 计算rsj,倒数第 m 根到倒数第一根， m 取13即为13:55至14:55；此处为小时内取高频值；
        rsj = df.groupby(df.index.strftime('%Y-%m-%d %H:00:00')).apply(lambda x: ((x[-m:-1][x[-m:-1] > 0] ** 2).sum() - (x[-m:-1][x[-m:-1] < 0] ** 2).sum()) / (x[-m:-1] ** 2).sum())
        # 用源数据整理结果需要的时间索引
        rsj_dt = df.reset_index().groupby(df.index.strftime('%Y-%m-%d %H:00:00')).first()
        # 给交易信号赋时间索引
        rsj.index = rsj_dt['date']

    else:   # elif strategy_type == "日频":
        # 计算rsj,倒数第 m 根到倒数第一根， m 取13即为13:55至14:55
        rsj = df.groupby(df.index.date).apply(lambda x: ((x[-m:-1][x[-m:-1] > 0] ** 2).sum() - (x[-m:-1][x[-m:-1] < 0] ** 2).sum()) / (x[-m:-1] ** 2).sum())

    rsj.index = pd.to_datetime(rsj.index)

    return rsj

