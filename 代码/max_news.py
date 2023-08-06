import heapq

def max_news(news_source,news_source_num,max_news_source,max_news_source_num):
    """获取新闻数量为前二十的新闻来源"""
    max_news_source_index = list(map(news_source_num.index,heapq.nlargest(20,news_source_num)))
    for i in max_news_source_index:
        max_news_source.append(news_source[i])
        max_news_source_num.append(news_source_num[i])