#-*- coding:utf-8 -*-
## 2018-10-30
## 拉勾网数据分析
import csv
import json
import pandas as pd
import re
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

# 读取数据
df = pd.read_csv('lagou_suanfa.csv', encoding='utf-8')
# 返回True或False
print(df['职位名称'].str.contains('实习'))
# 返回True的索引
print(df[df['职位名称'].str.contains('实习')].index)
# 数据清洗,剔除实习岗位
df.drop(df[df['职位名称'].str.contains('实习')].index, inplace=True)
# print(df.describe())
# 由于CSV文件内的数据是字符串形式,先用正则表达式将字符串转化为列表,再取区间的均值
pattern = '\d+'

df['work_year'] = df['工作经验'].str.findall(pattern)

# 数据处理后的工作年限
avg_work_year = []
# 工作年限
for i in df['work_year']:
   # 如果工作经验为'不限'或'应届毕业生',那么匹配值为空,工作年限为0
   if len(i) == 0:
       avg_work_year.append(0)
   # 如果匹配值为一个数值,那么返回该数值
   elif len(i) == 1:
       avg_work_year.append(int(''.join(i)))
   # 如果匹配值为一个区间,那么取平均值
   else:
       num_list = [int(j) for j in i]
       avg_year = sum(num_list)/2
       avg_work_year.append(avg_year)
df['工作经验'] = avg_work_year

# 将字符串转化为列表,再取区间的前25%，比较贴近现实
# print(df['工资'])
df['salary'] = df['工资'].str.findall(pattern)

# 月薪
avg_salary = []

for k in df['salary']:
   # int_list = [int(n) for n in k]
   int_list = [int(n) for n in k]
   avg_wage = int_list[0]+(int_list[1]-int_list[0])/4
   avg_salary.append(avg_wage)
df['月工资'] = avg_salary

# 将学历不限的职位要求认定为最低学历:大专
df['学历要求'] = df['学历要求'].replace('不限','大专')
"""
# 1、绘制频率直方图并保存
plt.hist(df['月工资'])
plt.xlabel('工资 (千元)')
plt.ylabel('频数')
plt.title("工资直方图")
plt.rcParams['font.sans-serif']=['SimHei']
plt.savefig('suanfa/薪资.jpg')
plt.show()

# 1、绘制频率直方图并保存
plt.hist(df['工作经验'])
plt.xlabel('工作年限')
plt.ylabel('频数')
plt.title("工作年限直方图")
plt.rcParams['font.sans-serif']=['SimHei']
plt.savefig('suanfa/工作经验.jpg')
plt.show()

# 2、绘制饼图并保存
count = df['区域'].value_counts()
plt.pie(count, labels = count.keys(),labeldistance=1.4,autopct='%2.1f%%')
plt.axis('equal')  # 使饼图为正圆形
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
plt.rcParams['font.sans-serif']=['SimHei']
plt.savefig('suanfa/分布区域.jpg')
plt.show()
"""
# 3、学历要求直方图
# {'本科': 1304, '大专': 94, '硕士': 57, '博士': 1}
dict = {}
for i in df['学历要求']:
    if i not in dict.keys():
        dict[i] = 0
    else:
        dict[i] += 1
index = list(dict.keys())
# print(index)
num = []
for i in  index:
    num.append(dict[i])
print('index:',index)
print('********************************************')
print('num:',num)
plt.bar(left=index, height=num, width=0.5)
plt.rcParams['font.sans-serif']=['SimHei']
plt.savefig('suanfa/学历.jpg')
plt.show()

# # 福利待遇词云图
# # 绘制词云,将职位福利中的字符串汇总
# text = ''
# for line in df['职位福利']:
#    text += line
# # 使用jieba模块将字符串分割为单词列表
# cut_text = ' '.join(jieba.cut(text))
# #color_mask = imread('cloud.jpg')  #设置背景图
# # print(cut_text)
# cloud = WordCloud(
#     background_color = 'white',
#     # 对中文操作必须指明字体
#     font_path='simkai.ttf',
#     #mask = color_mask,
#     max_words = 1000,
#     max_font_size = 100
#     ).generate(cut_text)
#
# # 保存词云图片
# cloud.to_file('suanfa/word_cloud.jpg')
# plt.imshow(cloud)
# plt.axis('off')
# plt.show()
