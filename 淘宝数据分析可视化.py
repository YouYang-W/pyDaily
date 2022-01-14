'''
某淘宝店共有10款商品，模拟生成该网店2019年的营业额数据，并将数据保存到磁盘文件data.csv
使用matplotlib绘制：
每一款商品的销售额折线图
按月统计各商品营业额并绘制柱状统计图
按季度统计各商品营业额并绘制饼状图
'''

import datetime
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 解决中文无法显示的问题
plt.rcParams['font.sans-serif']='SimHei'

def creat_sale():
    # 初始化时间
    date = datetime.date(2019, 1, 1)
    file = open('data.csv', 'w' ,encoding='gbk')
    harmonicons = ['Sp20', 'gm', 'boogieman', 'deepblue', 'M20', 'H20', 'MBC', 'MD1896', 'MBD', 'BigRiver']
    file.writelines('口琴种类,时间,销售额\n')

    for day in range(365):
        # 将每一种琴的销售额写入文件
        for harmonicon in harmonicons:
            file.writelines("{},{},{}\n".format(harmonicon, date, random.randint(0, 10)))
        # 天数加1
        date += datetime.timedelta(days=1)


def process_data_month():
    df = pd.read_csv('data.csv', header=0,encoding='gbk')
    df.set_index
    harmonicons = ['Sp20', 'gm', 'boogieman', 'deepblue', 'M20', 'H20', 'MBC', 'MD1896', 'MBD', 'BigRiver']
    # 对每种琴的销售额进行分月加和
    # dic = {'口琴种类':[1月销售额、2月...], ...}
    dic = {}
    for harmonicon in harmonicons:
        # 数据筛选
        df_h = df.loc[df['口琴种类']==harmonicon]
        # 数据加和
        df_h = df_h.groupby(lambda x:datetime.datetime.strptime(df_h['时间'][x], '%Y-%m-%d').month).sum()
        #print(df_h)
        dic[harmonicon] = list(df_h['销售额'])#dic是每个月各个琴的营销量
        #print(dic)
    return dic


def plot_first(data):
    harmonicons = ['Sp20', 'gm', 'boogieman', 'deepblue', 'M20', 'H20', 'MBC', 'MD1896', 'MBD', 'BigRiver']
    # 创建fig对象与ax对象
    fig, ax = plt.subplots(figsize=(14,7))#fig代表绘图窗口(Figure)；ax代表这个绘图窗口上的坐标系(axis)
    for i in range(10):
        # 依次绘图
        ax.plot(np.arange(1, 13), data[harmonicons[i]], label='{}'.format(harmonicons[i]))
    ax.set_xlabel('月份')
    ax.set_ylabel('销售额')
    ax.set_title('口琴销售额')
    ax.legend()

    plt.show()


def plot_second(data):
    harmonicons = ['Sp20', 'gm', 'boogieman', 'deepblue', 'M20', 'H20', 'MBC', 'MD1896', 'MBD', 'BigRiver']
    fig, ax = plt.subplots(figsize=(16,7))
    # 设置柱宽度
    width = 0.8/10
    for i in range(10):
        # 绘制柱状图
        ax.bar(np.arange(1, 13) + width*i, data[harmonicons[i]], width=width, label='{}'.format(harmonicons[i]))
    ax.set_title('口琴销售额')
    ax.legend()

    plt.show()

def plot_third(data):
    harmonicons = ['Sp20', 'gm', 'boogieman', 'deepblue', 'M20', 'H20', 'MBC', 'MD1896', 'MBD', 'BigRiver']
    # 数据重构
    for harmonicon in harmonicons:
        data[harmonicon] = [sum(data[harmonicon][i:i+3]) for i in range(0, 10, 3)]

    labels = ['第一季度', '第二季度', '第三季度', '第四季度']
    # 设置10个ax对象，在图上按2行5列排布
    fig, ax = plt.subplots(2, 5, figsize=(16,8))
    # 依次绘图
    for i in range(2):
        for j in range(5):
            ax[i][j].pie(data[harmonicons[i]], labels=labels, autopct='%1.1f%%')
            ax[i][j].set_title('{}口琴按季度销售额'.format(harmonicons[5*i+j]))
    plt.show()


def main():
    creat_sale()
    data_month = process_data_month()
    plot_first(data_month)
    plot_second(data_month)
    plot_third(data_month)


if __name__ == '__main__':
    main()