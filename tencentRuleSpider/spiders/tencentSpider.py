# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from tencentRuleSpider.items import TencentrulespiderItem

class TencentspiderSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0']

    rules = (
        Rule(LinkExtractor(allow='start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        nodes = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        for node in nodes:
            item = TencentrulespiderItem()
            item["name"] = node.xpath('./td[1]/a/text()').extract()[0]
            item["href"] = node.xpath('./td[1]/a/@href').extract()[0]
            item["type"] = node.xpath('./td[2]/text()').extract()
            item["hire_count"] = node.xpath('./td[3]/text()').extract()[0]
            item["local"] = node.xpath('./td[4]/text()').extract()[0]
            item["pub_time"] = node.xpath('./td[5]/text()').extract()[0]
            yield item
