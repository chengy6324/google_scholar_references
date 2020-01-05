# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs


class GoogleScholarReferencesPipeline(object):
    def __init__(self):
        self.file = codecs.open('paper_references.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(item['References']+'\n')
        return item

    def spider_closed(self, spider):
        self.file.close()
