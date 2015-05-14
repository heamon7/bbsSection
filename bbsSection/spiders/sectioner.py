# -*- coding: utf-8 -*-
import scrapy
from  bbsSection.items import BbssectionItem

class SectionerSpider(scrapy.Spider):
    name = "sectioner"
    allowed_domains = ["http://m.byr.cn/section"]
    start_urls = (
        'http://www.http://m.byr.cn/section/',
    )

    def parse(self, response):
        item = BbssectionItem()
        item['sectionListLink'] = response.xpath('//*[@id="m_main"]/ul/li/a[1]/@href').extract()
        item['sectionListName'] = response.xpath('//*[@id="m_main"]/ul/li/a[1]/text()').extract()

        return item
