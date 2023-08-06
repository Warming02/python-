import matplotlib.pyplot as plt

def drawing_plot(dates_month,portfolio_ratio):
    """绘制折线图"""
    plt.plot(dates_month,portfolio_ratio,'o-k',linewidth=2.5,label='portfolio_profit')
    plt.legend()
    plt.xticks(rotation=60)
    plt.xlabel("时间")
    plt.ylabel("收益率")
    plt.title("投资组合收益率")
    plt.savefig(r'C:/Users/未名/Desktop/python小组作业/月度收益率折线图')
    plt.clf()

def drawing_bar(dates_month,portfolio_ratio):
    """绘制柱状图"""
    plt.bar(dates_month,portfolio_ratio,color='b',label='portfolio_profit')
    plt.legend()
    plt.xticks(rotation=60)
    plt.xlabel("时间")
    plt.ylabel("收益率")
    plt.title("投资组合收益率")
    for a,b in zip(list(dates_month),portfolio_ratio):
        if b > 0:
            plt.text(a,b,'{:.2f}'.format(b),ha='center',va='bottom',fontsize=7)
        else:
            plt.text(a,b,'{:.2f}'.format(b),ha='center',va='top',fontsize=7)
    plt.savefig(r'C:/Users/未名/Desktop/python小组作业/月度收益率条形图')
    plt.clf()   

def drawing_bar_month(max_news_source,max_news_source_num):
    plt.bar(max_news_source,max_news_source_num,label='news_number')
    plt.legend()
    plt.xticks(fontsize=8,rotation=60)
    plt.xlabel("新闻来源")
    plt.ylabel("数量")
    plt.title("新闻来源数量")
    for a,b in zip(max_news_source,max_news_source_num):
        plt.text(a,b,b,ha='center',va='bottom',fontsize=7)
    plt.savefig(r'C:/Users/未名/Desktop/python小组作业/新闻来源总量')
    plt.clf()