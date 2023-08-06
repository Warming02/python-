import pandas as pd

def get_stocks_month(stocks_code,dates,dates_month,\
    stocks_df,stocks_month_df,stocks_month_profit_df,\
        stocks_month_news_df,stocks_month_forum_df,stocks_month):
    """获取股票的月度数据"""
    for i in range(len(stocks_df)):
        stock_month_df = pd.DataFrame({'股票代码':[stocks_code[i],] * 24,'时间':dates_month})
        stocks_month_df.append(stock_month_df)
        stocks_df[i]['month'] = dates.strftime('%Y-%m')

    for i in range(len(stocks_df)):
        grouped_stock_df = stocks_df[i].groupby(['股票代码','month'])
        news_forum_month = grouped_stock_df[['新闻数量','股吧发帖量']].sum().reset_index(drop=True)
        news_forum_month.columns= ['月度新闻数量','月度发帖量']
        stocks_month_news_df.append(stocks_month_df[i].join(news_forum_month['月度新闻数量']))
        stocks_month_forum_df.append(stocks_month_df[i].join(news_forum_month['月度发帖量']))
        price_ratio_month = []
        for j in dates_month:
            price = grouped_stock_df.get_group((stocks_code[i],j))['收盘价']
            not_null_price = price[price.notnull()]
            head_price = not_null_price.head(1).reset_index(drop=True)[0]
            tail_price = not_null_price.tail(1).reset_index(drop=True)[0]
            profit_ratio =  (tail_price-head_price)/head_price
            price_ratio_month.append(profit_ratio)
        stocks_month_profit_df.append(stocks_month_df[i].join(pd.Series(price_ratio_month,name='月度收益率')))
        stocks_month_df[i]['月度收益率'] = price_ratio_month
        stocks_month_df[i] = stocks_month_df[i].join(news_forum_month)

    for i in stocks_month_df:
        stocks_month = stocks_month.append(i,ignore_index=True)
    
    return stocks_month