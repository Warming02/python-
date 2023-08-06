import pandas as pd
import re

def get_forum(forum_path,stocks_code,stocks_forum_df):
    """获取所有股票代码的股吧数量数据"""
    stocks_pattern = []
    for i in range(len(stocks_code)):
        stock_code = stocks_code[i]
        pattern = re.compile(stock_code)
        stocks_pattern.append(pattern)

    stocks_forum_num = []
    for i in range(len(stocks_code)):
        stock_forum_num = [None]*365
        stocks_forum_num.append(stock_forum_num)

    #遍历发帖数据
    for i in range(1,366):
        #读取该天的发帖数据
        path = forum_path.format(number=i)
        forum_file = pd.read_csv(path)
        #获取每只股票的发帖数据
        for j in range(len(stocks_code)):
            for k in range(len(forum_file)):
                match = stocks_pattern[j].search(forum_file['CODE NUM'][k])
                if match:
                    index = k
                    break
            if (match == None) and (k == len(forum_file)-1):
                    stocks_forum_num[j].append(0)
            else:
                pattern = re.compile(r'\d+$')
                match = pattern.search(forum_file['CODE NUM'][index])
                stocks_forum_num[j].append(int(match.group(0)))
    
    for i in stocks_forum_num:
        stocks_forum_df.append(pd.Series(i))


