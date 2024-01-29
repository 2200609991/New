"""
自行编辑的本地文件
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# 设置全部可视化
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

start_date = '2018-11-23'
# end_date = '2021-05-25'
end_date = '2019-01-02'
index_code = '000300.XSHG'

# 获取指数5分钟数据
# stock = get_price(index_code,start_date=start_date,end_date=pd.to_datetime(end_date)+datetime.timedelta(days=1),frequency='5min',fields=['close'])
stock = pd.read_csv('data/hs300.csv')
stock = stock.set_index('date')[['close']]
stock.index = pd.DatetimeIndex(stock.index)
"""
                       close
date                        
2018-11-23 14:35:00  3156.97
2018-11-23 14:40:00  3150.45
2018-11-23 14:45:00  3148.44
2018-11-23 14:50:00  3148.05
"""

# 计算5分钟收益率
stock['ret'] = stock['close'].pct_change()
# 获取指数日数据
# stock_day = get_price(index_code,start_date=start_date,end_date=end_date,frequency='D',fields=['close'])
# stock_day.to_csv('data/stock_day.csv')
# stock_day = pd.read_csv('data/stock_day.csv',index_col=0)
# stock_day = pd.read_csv('data/000300.XSHG.csv',index_col=0)
stock_day = pd.read_pickle('data/000300_SH.pickle')['close']
stock_day = stock_day[stock_day.index <= end_date]
"""
                       close       ret
date                                  
2018-11-23 14:35:00  3156.97       NaN
2018-11-23 14:40:00  3150.45 -0.002065
2018-11-23 14:45:00  3148.44 -0.000638
2018-11-23 14:50:00  3148.05 -0.000124
"""

# 计算未来一天的收益率
# 计算rsj 倒数第13根到倒数第一根，即13:55至14:55
rsj = stock['ret'].groupby(stock.index.date)

m = 13  # 12个值每组
rsj = stock['ret'].groupby(stock.index.date).apply(
        lambda x: ((x[-m:-1][x[-m:-1] > 0]**2).sum()
                   - (x[-m:-1][x[-m:-1] < 0]**2).sum())/(x[-m:-1]**2).sum())
"""
2018-11-23   -1.000000
2018-11-26   -0.077450
2018-11-27   -0.131333
2018-11-28    0.281437
2018-11-29   -0.432708
"""
# stock_day['rsj'] = rsj.values
# rsj.index = list(str(i) for i in rsj.index)
stock_day = pd.merge(stock_day, pd.DataFrame(rsj).rename(columns={'ret': 'rsj'}), left_index=True, right_index=True)
stock_day['future_ret'] = stock_day['close'].pct_change().shift(-1)

stock_day['future_ret'].iloc[0] = 0  # 23号数据不足1小时,应该剔除
stock_day['symbol'] = (stock_day['rsj'] < 0).astype('int')

"""
                close       rsj  future_ret  symbol
2018-11-23  3143.4752 -1.000000    0.000000       1
2018-11-26  3141.2434 -0.077450   -0.001274       1
2018-11-27  3137.2413 -0.131333    0.013289       1
2018-11-28  3178.9326  0.281437   -0.012985       0
2018-11-29  3137.6542 -0.432708    0.011166       1
2018-11-30  3172.6900  0.706778    0.027819       0
2018-12-03  3260.9502 -0.012609    0.002073       1
"""
result = dict()
# 资金曲线,多头,空头,多空择时
result['long'] = ((stock_day['future_ret']*(-1)*np.sign(stock_day['rsj'].fillna(0)).replace(1, 0))+1).cumprod()
result['short'] = ((stock_day['future_ret']*(-1)*np.sign(stock_day['rsj'].fillna(0)).replace(-1, 0))+1).cumprod()
result['long_short'] = ((stock_day['future_ret']*(-1)*np.sign(stock_day['rsj'].fillna(0)))+1).cumprod()
result['original'] = (stock_day['future_ret']+1).cumprod()
# 每日收益率
result['long_ret'] = (stock_day['future_ret']*(-1)*np.sign(stock_day['rsj'].fillna(0)).replace(1, 0))
result['short_ret'] = (stock_day['future_ret']*(-1)*np.sign(stock_day['rsj'].fillna(0)).replace(-1, 0))
result['long_short_ret'] = (stock_day['future_ret']*(-1)*np.sign(stock_day['rsj'].fillna(0)))
rsj.index = pd.DatetimeIndex(rsj.index)
result['rsj'] = rsj[rsj.index <= end_date]
result = pd.DataFrame(result)
# print(result)
"""
                long     short  long_short  original  long_ret  short_ret  long_short_ret       rsj
2018-11-23  1.000000  1.000000    1.000000  1.000000  0.000000  -0.000000        0.000000 -1.000000
2018-11-26  0.998726  1.000000    0.998726  0.998726 -0.001274   0.000000       -0.001274 -0.077450
2018-11-27  1.011998  1.000000    1.011998  1.011998  0.013289  -0.000000        0.013289 -0.131333
2018-11-28  1.011998  1.012985    1.025139  0.998857  0.000000   0.012985        0.012985  0.281437
2018-11-29  1.023298  1.012985    1.036586  1.010011  0.011166  -0.000000        0.011166 -0.432708
2018-11-30  1.023298  0.984805    1.007749  1.038108 -0.000000  -0.027819       -0.027819  0.706778
2018-12-03  1.025419  0.984805    1.009838  1.040260  0.002073  -0.000000        0.002073 -0.012609
2018-12-04  1.025419  0.989538    1.014692  1.035260  0.000000   0.004806        0.004806  0.722766
2018-12-05  1.025419  1.010939    1.036637  1.012871  0.000000   0.021627        0.021627  0.429371
2018-12-06  1.025385  1.010939    1.036601  1.012836 -0.000034   0.000000       -0.000034 -0.160690
2018-12-07  1.025385  1.022633    1.048592  1.001120  0.000000   0.011567        0.011567  0.239603
2018-12-10  1.025385  1.017738    1.043573  1.005912 -0.000000  -0.004787       -0.004787  0.094717
2018-12-11  1.025385  1.014261    1.040008  1.009348 -0.000000  -0.003416       -0.003416  0.802440
2018-12-12  1.025385  0.998560    1.023908  1.024974 -0.000000  -0.015481       -0.015481  0.358780
2018-12-13  1.008257  0.998560    1.006805  1.007853 -0.016704   0.000000       -0.016704 -0.505333
2018-12-14  1.006755  0.998560    1.005305  1.006352 -0.001489   0.000000       -0.001489 -0.698014
2018-12-17  1.006755  1.008911    1.015727  0.995920  0.000000   0.010366        0.010366  0.365833
2018-12-18  1.006755  1.020941    1.027837  0.984045  0.000000   0.011923        0.011923  0.531207
2018-12-19  0.999034  1.020941    1.019954  0.976498 -0.007670   0.000000       -0.007670 -0.674812
2018-12-20  0.986650  1.020941    1.007311  0.964394 -0.012395   0.000000       -0.012395 -0.129229
2018-12-21  0.986650  1.017974    1.004384  0.967196 -0.000000  -0.002906       -0.002906  0.310107
2018-12-24  0.986650  1.024982    1.011299  0.960537  0.000000   0.006885        0.006885  0.795406
2018-12-25  0.986650  1.030162    1.016410  0.955683  0.000000   0.005054        0.005054  0.530783
2018-12-26  0.986650  1.034118    1.020313  0.952013  0.000000   0.003840        0.003840  0.499565
2018-12-27  0.993297  1.034118    1.027187  0.958427  0.006737  -0.000000        0.006737 -0.045113
2018-12-28  0.979731  1.034118    1.013158  0.945338 -0.013658   0.000000       -0.013658 -0.188486
2019-01-02       NaN       NaN         NaN       NaN       NaN        NaN             NaN  0.473993
"""
exit()
result1=result.pct_change()
result.to_csv("result/output.csv")
N = 252
df_nav = result.dropna(axis=0, how='all')
yret = df_nav.iloc[-1] ** (N / len(df_nav))-1
Sharp = df_nav.pct_change().mean() / df_nav.pct_change().std() * np.sqrt(N)
df0 = df_nav.shift(1).fillna(1)
MDD = (1 - df0 / df0.cummax()).max()
Calmar = yret / MDD

df_nav.columns = [result.columns[i]
              + '\nyret:' + "%.2f%%" % (yret[i] * 100)
              + '  Sharp:{}'.format(round(Sharp[i], 2))
              + '\nMDD:' + "%.2f%%" % (MDD[i] * 100)
              + '  Calmar:{}'.format(round(Calmar[i], 2))
              for i in range(result.shape[1])
              ]
df_nav.plot(figsize=(10, 8), title=index_code)
plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0)
plt.savefig('result/回测结果.png')
plt.show()

