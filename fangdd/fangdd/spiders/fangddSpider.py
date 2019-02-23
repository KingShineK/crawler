# -*- coding: utf-8 -*-
import scrapy
from fangdd.items import FangddItem

class FangddspiderSpider(scrapy.Spider):
    name = 'fangddSpider'
    allowed_domains = ['fangdd.com']
    start_urls = ['https://beijing.fangdd.com/loupan/']
    # 构造爬取的网页地址
    page = 68
    url = 'https://beijing.fangdd.com/loupan/?pageNo='
    for i in range(2, page+1):
        start_urls.append(url + str(i))
    # print(start_urls)

    def parse(self, response):
        node_list = response.xpath("//div[@class='LpList-cont']")

        for node in node_list:
            item = FangddItem()

            # 爬取四个字段
            item['name'] = node.xpath("./h4/a/text()").extract()[0]
            item["region"] = node.xpath("./p[@class='LpList-address ellipsis']/a/text()").extract()[0]

            s_pricelist = node.xpath("./div[@class='LpList-pricebox']/p[@class='LpList-price LpList-price-main']/strong/text()").extract()
            item["s_price"] = ''.join(s_pricelist)

            t_pricelist = node.xpath("./div[@class='LpList-pricebox']/p[@class='LpList-price-sub']/text()").extract()
            item["t_price"] = ''.join(t_pricelist)

            arealist = node.xpath("./p[@class='LpList-type']/text()").extract()
            item["area"] = ''.join(arealist)

            yield item
