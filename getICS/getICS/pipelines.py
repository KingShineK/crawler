# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import csv

class GeticsPipeline(object):
    def __init__(self):
        # self.f = open("getProxy.json","w")
        self.icss = []
        print("开始导出到CSV......")
    def process_item(self, item, spider):
        # content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        # 将总数据转化为data frame再输出
        ics = [item['title'],item["level"],item["clicks"],item["date"]]

        self.icss.append(ics)

    def close_spider(self,spider):
        # self.f.close()
        df = pd.DataFrame(data=self.icss,
                          columns=['漏洞标题', '危害级别', '点击数', '时间'])
        df.to_csv('ics.csv', index=False, encoding='utf-8_sig')
        print("导出成功！")

