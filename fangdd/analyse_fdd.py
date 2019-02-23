import csv
import json
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

# 读取数据
df = pd.read_csv('beijing/fangdd.csv', encoding='utf-8',usecols=['楼盘名称','楼盘位置','单价'])
# print(df.describe())
# 查询某值所在的数据行
# print(df.loc[df[df['单价']==385306].index])
# # 统计不重复出现的个数
# print(df['楼盘位置'].value_counts())
# print(df['楼盘位置'].count())

# 数据清洗,去除位置、单价为空的数据
# df.dropna(axis=0,how='any',inplace=True)
#
# # 将惠城区、海港区、涿州市、香河县并入北京周边
# county=['惠城区','海港区','涿州市','香河县','河东区','固安县','津南区','滨海新区','莲池区','三河市','北戴河区',
#     '仲恺区','抚宁区','澄海区','广阳区','招远区','静海区','双桥区','开平区','招远市','西青区','东丽区',
#     '和县','安次区','霸州市','定兴县','云岗','南开区','文昌区','古城区','固安','竞秀区','怀来县','右安门',
#     '惠阳区','武清区','涞水县','文昌市','和平区','呈贡区','怀安县']
#
# for ct in county:
#     df.drop(df[df['楼盘位置'].str.contains(ct)].index,inplace=True)
#
# print(df['楼盘位置'].count())
# # print(df.head())
# # 1、绘制统计的各区房屋数量饼图
# count = df['楼盘位置'].value_counts()
# plt.pie(count, labels = count.keys(),labeldistance=1.4,autopct='%2.1f%%')
# plt.axis('equal')  # 使饼图为正圆形
# plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.title('2019年1月北京各区楼盘位置分布图')
# plt.savefig('beijing/各区楼盘位置分布图.jpg')
# plt.show()
#
# # 2、绘制各区房价均价直方图
# # 根据楼盘位置分组求价格平均值
# df_mean = df.groupby(['楼盘位置'],as_index=False)['单价'].mean()
# region = df_mean['楼盘位置']
# s_price = df_mean['单价']
#
# plt.bar(left=region, height=s_price, width=0.5)
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.title('2019年1月北京各区房价直方图')
# plt.xlabel('区县名称')
# plt.ylabel('单价（元/米2）')
# plt.savefig('beijing/各区房价直方图.jpg')
# # 添加柱上具体数值
# for a,b in zip(region,s_price):
#     plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=11)
# plt.show()
#
# # 3、绘制各区楼盘房价最高价和最低价
# df_grop = df.groupby(['楼盘位置'],as_index=False)['单价']
# df_max = df_grop.max()
# # print(df_grop)
# df_min = df_grop.min()
# region = df_grop.count()['楼盘位置']
# max_price = df_max['单价']
# min_price = df_min['单价']
# # print(index,list(region))
#
# index = np.arange(len(region))
# bar_width = 0.35
# plt.bar(left=index, height=max_price, width=bar_width, label='最高值')
# plt.bar(left=index + bar_width, height=min_price, width=bar_width, label='最低值')
# plt.xticks(index,list(region))
#
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.title('2019年1月北京各区房价直方图')
# plt.xlabel('区县名称')
# plt.ylabel('单价（元/米2）')
# # 添加柱上具体数值
# for a,b in zip(index,max_price):
#     plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=11)
# for a,b in zip(index,min_price):
#     plt.text(a+bar_width, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=11)
#
# plt.legend()
# plt.savefig('beijing/各区房价最高值最低值直方图.jpg')
# plt.show()
