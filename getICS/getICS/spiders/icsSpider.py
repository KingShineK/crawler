# -*- coding: utf-8 -*-
import scrapy
from getICS.items import GeticsItem

class IcsspiderSpider(scrapy.Spider):
    name = 'icsSpider'
    allowed_domains = ['ics.cnvd.org.cn']
    start_urls = ['http://ics.cnvd.org.cn/']

    # 构造爬取的网页地址
    page = 94
    url = 'http://ics.cnvd.org.cn/?max=20&offset='
    for i in range(1,page):
        start_urls.append(url + str(20*i))

    # print("************************************************************************")
    # print(start_urls)

    def parse(self, response):
        node_list = response.xpath("//tbody/tr")

        for node in node_list:
            item = GeticsItem()

            # 爬取四个字段，标题、危险等级、点击数、时间
            item['title'] = node.xpath("./td[1]/a/text()").extract()[0].replace('\r','').replace('\n','').replace('\t','').replace(' ','')
            item["level"] = node.xpath("./td[2]/text()").extract()[1].replace('\r','').replace('\n','').replace('\t','').replace(' ','')
            item["clicks"] = node.xpath("./td[3]/text()").extract()[0]
            item["date"] = node.xpath("./td[6]/text()").extract()[0].replace('\r','').replace('\n','').replace('\t','').replace(' ','')

            yield item

