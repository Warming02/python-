import pandas as pd

def get_tonghuashun_data(news_path,stocks_code,tonghuashun_data,ths_pattern):
    """获取同花顺新闻来源的新闻数据"""
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
                for k in range(length):
                    match = ths_pattern.search(news_file['source_doc'][k])
                    if match:
                        tonghuashun_data = tonghuashun_data.append(news_file.loc[k],ignore_index=True)
            except FileNotFoundError:pass
    
    return tonghuashun_data