# -*- coding: utf-8 -*-
import scrapy
from  bbsSection.items import BbssectionItem
from scrapy.shell import inspect_response
class SectionerSpider(scrapy.Spider):
    name = "sectioner"
    allowed_domains = ["m.byr.cn/section"]
    start_urls = (
        'http://m.byr.cn/section/',
    )

    def parse(self, response):
        item = BbssectionItem()
      #  inspect_response(response,self)
        item['sectionListLink'] = response.xpath('//*[@id="m_main"]/ul/li/a[1]/@href').extract()
        item['sectionListName'] = response.xpath('//*[@id="m_main"]/ul/li/a[1]/text()').extract()
      #  print item['sectionListLink']
        return item
