# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query
from scrapy import log
from scrapy.exceptions import DropItem
from bbsSection import settings


class SectionPipeline(object):
    def __init__(self):
        leancloud.init(settings.APP_ID, master_key=settings.MASTER_KEY)

        pass
    def process_item(self, item, spider):

        Sections = Object.extend('Sections')
        for index in range(len(item['sectionListLink'])):
            section = Sections()
            query = Query(Sections)
            query.equal_to('sectionLink',item['sectionListLink'][index])
            try:
                if  query.find():
                    pass
                else:
                    section.set('sectionLink',item['sectionListLink'][index])
                    section.set('sectionName',item['sectionListName'][index])
                    try:
                        section.save()
                    except LeanCloudError,e:
                        print e
            except LeanCloudError,e:
                print e

        DropItem()
