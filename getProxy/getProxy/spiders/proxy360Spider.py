# -*- coding: utf-8 -*-
import scrapy
from getProxy.items import GetproxyItem

class Proxy360spiderSpider(scrapy.Spider):
    name = 'proxy360Spider'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/1',
                  'https://www.xicidaili.com/nn/2',
                  'https://www.xicidaili.com/nn/3',
                  'https://www.xicidaili.com/nn/4',
                  'https://www.xicidaili.com/nn/5',
                  ]

    def parse(self, response):
        node_list = response.xpath("//tr[@class='odd']|//tr[@class='']")

        for node in node_list:
            item = GetproxyItem()

            item['ip'] = node.xpath("./td[2]/text()").extract()[0]
            item["port"] = node.xpath("./td[3]/text()").extract()[0]
            item["type"] = node.xpath("./td[5]/text()").extract()[0]
            item["protocol"] = node.xpath("./td[6]/text()").extract()[0]

            yield item
