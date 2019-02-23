# -*- coding: utf-8 -*-
import scrapy
from getCII.items import GetciiItem


class CiichinaSpider(scrapy.Spider):
    name = 'ciiChina'
    allowed_domains = ['cac.gov.cn']
    # start_urls = ['http://cac.gov.cn/',
    #               'http://www.cac.gov.cn/2017-07/11/c_1121294220.htm',
    #               'http://www.cac.gov.cn/2016-12/27/c_1120195926.htm']
    start_urls = ['http://www.cac.gov.cn/2016-12/27/c_1120195926.htm']

    def parse(self, response):
        item = GetciiItem()
        item['title'] = response.xpath("//h1[@id='title']").extract()[0]

        content = response.xpath("//div[@id='content']")
        item['content'] = content.extract()[0]

        conts = []
        node_list = content.xpath("//strong")
        for node in node_list:
            conts.append(node.extract())

        item['sec_title'] = ''.join(conts)
        # print(item['sec_title'])

        yield item
