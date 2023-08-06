import pandas as pd

def get_vol(vol_path,stocks_code,stocks_vol_df):
    """获取所有股票代码的成交量"""
    
    vol_df = pd.read_excel(vol_path)
    dates = pd.date_range(start='2014-01-01',end='2015-12-31',freq='D')
    for i in range(len(stocks_code)):
        stock_code = stocks_code[i]
        stock_df = pd.DataFrame({'股票代码':[stock_code] * 365 * 2,'时间':dates})
        #将datetime64[ns]类型转换为字符串类型
        stock_df['时间'] = stock_df['时间'].astype(str)
        stock_vol = vol_df[stock_code].to_frame().join(vol_df['Date'])
        stock_vol.columns = ['成交量','时间']
        stock_df = pd.merge(stock_df,stock_vol,how='outer')
        stocks_vol_df.append(stock_df)

