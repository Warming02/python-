import pandas as pd
import re

def get_news(news_path,stocks_code,stocks_news_df):
    """获取所有股票代码的新闻数量数据"""
    news_date = pd.date_range(start='2015-01-01',end='2015-12-31',freq='D')
    date_string = r'{date:s}.pkl'
    stocks_news_num = []
    for i in range(len(stocks_code)):
        stock_news_num = [None]*365
        stocks_news_num.append(stock_news_num)

    for i in range(len(stocks_code)):
        filename_news = news_path.format(stock_number=stocks_code[i][:6])
        for j in news_date:
            path = filename_news + date_string.format(date=j.strftime('%F'))
            try:
                #当该天有新闻时
                news_file = pd.read_pickle(path)
                length = len(news_file['source_doc'][news_file['source_doc'].notnull()])
                stocks_news_num[i].append(length)
            except FileNotFoundError:
                #当该天的新闻不存在时，新闻数量计为0
                stocks_news_num[i].append(0)

    for i in stocks_news_num:
        stocks_news_df.append(pd.Series(i))


            