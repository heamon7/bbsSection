# -*- coding: utf-8 -*-
import scrapy
from  bbsSection.items import BbssectionItem
from scrapy.shell import inspect_response
import os

import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query


class SectionerSpider(scrapy.Spider):
    name = "sectioner"
    allowed_domains = ["m.byr.cn/section"]
    start_urls = (
        'http://m.byr.cn/section/',
    )
    def __init__(self,stats):
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def parse(self, response):
        item = BbssectionItem()
      #  inspect_response(response,self)
        item['sectionListLink'] = response.xpath('//*[@id="m_main"]/ul/li/a[1]/@href').extract()
        item['sectionListName'] = response.xpath('//*[@id="m_main"]/ul/li/a[1]/text()').extract()
      #  print item['sectionListLink']
        return item

    def closed(self,reason):
        #f = open('../../nohup.out')
        #print f.read()
        leancloud.init('yn33vpeqrplovaaqf3r9ttjl17o7ej0ywmxv1ynu3d1c5wk8', master_key='zkw2itoe7oyyr3vmyrs8m95gbk0azmikc3jrtk2lw2z4792i')
        try:
            nohupOut = open(os.getcwd()+'/nohup.out','r').read()
        except:
            nohupOut = "Cannot read nohup.out file"
        CrawlerLog = Object.extend('CrawlerLog')
        crawlerLog = CrawlerLog()

        crawlerLog.set('crawlerName',self.name)
        crawlerLog.set('crawlerLog',nohupOut)
        crawlerLog.set('crawlerStats',self.stats.get_stats())

