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

class SectionPipeline(object):
    def __init__(self):
        leancloud.init('mctfj249nwy7c1ymu3cps56lof26s17hevwq4jjqeqoloaey', master_key='ao6h5oezem93tumlalxggg039qehcbl3x3u8ofo7crw7atok')

    def process_item(self, item, spider):

        Sections = Object.extend('Sections')
        section = Sections()
        for index in len(item['sectionListLink']):
            try:
                section.set('sectionLink',item['sectionListLink'][index])
                section.set('sectionName',item['sectinListName'][index])
                section.save()
            except LeanCloudError,e:
                print e

        return item
