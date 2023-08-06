import pandas as pd

def get_news_source(news_path,stocks_code,news_source,news_source_num):
    """获取股票新闻来源"""
    news_date = pd.date_range(start='2015-01-01',end='2015-12-31',freq='D')
    date_string = r'{date:s}.pkl'

    for i in range(len(stocks_code)):
        filename_news = news_path.format(stock_number=stocks_code[i][:6])
        for j in news_date:
            path = filename_news + date_string.format(date=j.strftime('%F'))
            try:
                #当该天有新闻时
                news_file = pd.read_pickle(path)
                length = len(news_file['source_doc'][news_file['source_doc'].notnull()])
                #遍历新闻来源并计算数量
                for j in range(length):
                    try:
                        #当该新闻来源存在于news_source中时
                        pos = news_source.index(news_file['source_doc'][j])
                        news_source_num[pos] +=1
                    except ValueError:
                        #当该新闻来源不存在于news_source中时
                        news_source.append(news_file['source_doc'][j])
                        news_source_num.append(1)
            except FileNotFoundError:pass
    