import pandas as pd

def integration(stocks_code,dates,stocks_price_df,stocks_vol_df\
            ,stocks_news_df,stocks_forum_df,stocks_df,stocks):
        """将股票所有信息整合起来"""
        for i in range(len(stocks_code)):
            stock_df = pd.DataFrame({'股票代码':[stocks_code[i]] * 365 * 2,'时间':dates})
            #将datetime64[ns]类型转换为字符串类型
            stock_df['时间'] = stock_df['时间'].astype(str)
            stock_df = pd.merge(stock_df,stocks_price_df[i],how='outer')
            stock_df = pd.merge(stock_df,stocks_vol_df[i],how='outer')
            stock_df['新闻数量'] = stocks_news_df[i]
            stock_df['股吧发帖量'] = stocks_forum_df[i]
            stocks_df.append(stock_df)
            stocks = stocks.append(stock_df,ignore_index=True)
        return stocks