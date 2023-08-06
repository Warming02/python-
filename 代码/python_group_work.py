import re
import copy
import heapq
import pandas as pd
import matplotlib.pyplot as plt
from forum import get_forum
from news import get_news
from price import get_price
from vol import get_vol
from integration import integration
from stocks_month import get_stocks_month
from drawing import drawing_plot,drawing_bar,drawing_bar_month
from max_news import max_news
from news_source import get_news_source
from tonghuashun import get_tonghuashun_data
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

dates = pd.date_range(start='2014-01-01',end='2015-12-31',freq='D')
stocks_code = ['000001.SZ','000002.SZ','000004.SZ','000005.SZ',
    '000006.SZ','000007.SZ','000008.SZ','000009.SZ','000011.SZ',
    '000012.SZ','600000.SH','600004.SH','600006.SH','600007.SH',
    '600008.SH','600009.SH','600010.SH','600011.SH','600012.SH','600015.SH']
price_path = r'C:/Users/未名/Desktop/python小组作业/price.xlsx'
vol_path =  r'C:/Users/未名/Desktop/python小组作业/VOL.xlsx'
news_path = r'C:/Users/未名/Desktop/python小组作业/新闻数据/{stock_number:s}/'
forum_path = r'C:/Users/未名/Desktop/python小组作业/发帖数据/2015-01-01 ({number}).txt'

#第一题:
#股票价格表
stocks_price_df = []
#股票成交量表
stocks_vol_df = []
#股票新闻数量表
stocks_news_df = []
#股票股吧数量表
stocks_forum_df = []
#容纳各股的数据表格
stocks_df = []
#股票数据表(第一题答案)
stocks = pd.DataFrame()

get_price(price_path,stocks_code,stocks_price_df)
get_vol(vol_path,stocks_code,stocks_vol_df)
get_news(news_path,stocks_code,stocks_news_df)
get_forum(forum_path,stocks_code,stocks_forum_df)
stocks = integration(stocks_code,dates,stocks_price_df,stocks_vol_df,\
            stocks_news_df,stocks_forum_df,stocks_df,stocks)

#将股票数据保存为Excel文件
writer = pd.ExcelWriter(r'C:/Users/未名/Desktop/python小组作业/stocks.xlsx')
stocks.to_excel(writer,sheet_name='stocks_data',index=False)
writer.close()

#第二，三，四，五题:
#各股的月度收益率
stocks_month_profit_df = []
#各股的月度新闻数量
stocks_month_news_df = []
#各股的月度发帖数量
stocks_month_forum_df = []
#容纳各股的月度数据表格
stocks_month_df = []
#各股的月度数据表格（）
stocks_month = pd.DataFrame()
#月度时间
dates_month = pd.date_range(start='2014-01-01',end='2015-12-31',freq='M').strftime('%Y-%m')

stocks_month = get_stocks_month(stocks_code,dates,dates_month,\
                    stocks_df,stocks_month_df,stocks_month_profit_df,\
                    stocks_month_news_df,stocks_month_forum_df,stocks_month)

#将股票月度数据保存为Excel文件
writer = pd.ExcelWriter(r'C:/Users/未名/Desktop/python小组作业/stocks_month.xlsx')
stocks_month.to_excel(writer,sheet_name='stocks_month_data',index=False)
writer.close()

#第六题：

#投资组合月度收益率
portfolio_ratio = []
for i in range(len(dates_month)):
    portfolio = 0
    for j in stocks_month_profit_df:
        portfolio += j['月度收益率'][i]
    portfolio_ratio.append(portfolio)

#绘制折线图
drawing_plot(dates_month,portfolio_ratio)
#绘制条形图
drawing_bar(dates_month,portfolio_ratio)

#第七题:
#新闻来源变量
news_source = []
#新闻来源的数量
news_source_num = []
#前二十位新闻数量最多的新闻来源
max_news_source = []
#前二十位新闻来源的数量
max_news_source_num = []

get_news_source(news_path,stocks_code,news_source,news_source_num)
max_news(news_source,news_source_num,max_news_source,max_news_source_num)
drawing_bar_month(max_news_source,max_news_source_num)

#第八题:
#同花顺的新闻数据
tonghuashun_data = pd.DataFrame()
ths_pattern = re.compile(r"同花顺|同花顺财经")
tonghuashun_data = get_tonghuashun_data(news_path,stocks_code,tonghuashun_data,ths_pattern)
writer = pd.ExcelWriter(r'C:/Users/未名/Desktop/python小组作业/同花顺.xlsx')
tonghuashun_data.to_excel(writer,sheet_name='tonghuashun_data',index=False)
writer.close()














