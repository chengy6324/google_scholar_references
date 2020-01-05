# -*- coding: utf-8 -*-
import scrapy
import logging
from ..items import GoogleScholarReferencesItem
import re


class GooglespiderSpider(scrapy.Spider):
    name = 'googlespider'

    def __init__(self, paperlist=None, *args, **kwargs):
        super(GooglespiderSpider, self).__init__(*args, **kwargs)
        file = open('./'+paperlist, encoding='utf-8')
        self.file_line = [line.rstrip() for line in file]

    def start_requests(self):
        url_a_prefix = 'https://scholar.google.com/scholar?start=0&q='
        url_a_postfix = '&hl=zh-CN&as_sdt=0,5'
        for i in self.file_line:
            yield scrapy.Request(url=url_a_prefix+i.replace(' ', '+')+url_a_postfix, callback=self.parse)

    def parse(self, response):
        url_prefix = 'https://scholar.google.com/scholar?q=info:'
        url_mid = ':scholar.google.com/&output=cite&scirp='
        url_postfix = '&hl=zh-CN'
        all_list = response.css('#gs_res_ccl_mid div::attr(data-cid)').extract_first()
        all_list_n = response.css('#gs_res_ccl_mid div::attr(data-rp)').extract_first()
        url_join = url_prefix + all_list + url_mid + all_list_n + url_postfix
        yield scrapy.Request(url=url_join, callback=self.parse_references)

    def parse_references(self, response):
        item_reference = GoogleScholarReferencesItem()
        item_reference['References'] = response.css('#gs_citt div::text').extract()[0]
        yield item_reference


