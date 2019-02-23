# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import re
from w3lib.html import remove_tags

class GetciiPipeline(object):
    def __init__(self):
        self.f = open("getCII.json","w",encoding='utf-8')

    def process_item(self, item, spider):

        title = remove_tags(item['title']).replace('\r\n','')
        sec_title = remove_tags(item['sec_title']).replace('\r\n', '')
        content = remove_tags(item['content']).replace('\r\n','')


        full_text = {'title':title,'content':content,'sec_title':sec_title}

        full_text = json.dumps(full_text, ensure_ascii=False)
        self.f.write(full_text)
        # print(full_text)
        # return item

    def close_spider(self,spider):
        self.f.close()
