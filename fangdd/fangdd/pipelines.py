# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import csv

class FangddPipeline(object):
    def __init__(self):

        self.fdds = []
        print("开始导出到CSV......")
    def process_item(self, item, spider):
        # 将总数据转化为data frame再输出
        fdd = [item['name'],item["region"],item["s_price"],item["t_price"],item["area"]]

        self.fdds.append(fdd)

    def close_spider(self,spider):
        # self.f.close()
        df = pd.DataFrame(data=self.fdds,
                          columns=['楼盘名称', '楼盘位置', '单价', '总价','面积'])
        df.to_csv('北京/fangdd.csv', index=False, encoding='utf-8_sig')
        print("导出成功！")
