# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class GetproxyPipeline(object):
    def __init__(self):
        self.f = open("getProxy.json","w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False) + ",\n"
        self.f.write(content)
        return item

    def close_spider(self,spider):
        self.f.close()

class GetproxyPipelineTxt(object):
    def process_item(self, item, spider):
        fileName = 'proxy.txt'
        with open(fileName,'a') as fp:
            fp.write(item['ip'].strip()+'\t')
            fp.write(item['port'].strip() + '\t')
            fp.write(item['protocol'].strip() + '\t')
            fp.write(item['type'].strip() + '\n')
        return item
