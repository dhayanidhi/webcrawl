# -*- coding: utf-8 -*-
import scrapy
from webscrap.items import KeywordItem
import urllib.parse
import os


class PubNlmSpider(scrapy.Spider):
    name = 'pub_nlm'
    allowed_domains = ['pubmed.ncbi.nlm.nih.gov']

    def start_requests(self):
        url = 'https://pubmed.ncbi.nlm.nih.gov/'
        tag = os.environ['AUTHOR']
        if tag is not None:
            url = url + '?term=' + urllib.parse.quote(tag) + '&size=200'
        self.logger.info("new url "+ url)
        yield scrapy.Request(url, self.parse)


    def parse(self, response):
        for link in response.xpath('//*[@id="search-results"]/section/div[1]/div/article[@class="labs-full-docsum"]/div[2]/div[1]/a/@href').getall():
            extracted_link = response.urljoin(link)
            self.logger.info("execute link " + extracted_link)
            yield scrapy.Request(extracted_link, self.parse_sub_link)

    def parse_sub_link(self, response):
        keywords = response.xpath('//*[@id="abstract"]/p/text()').getall()
        result_keyword = filter(lambda x: len(x.strip()) > 0, keywords)
        result = list()
        for item in result_keyword:
            result.extend(list(map(lambda x: x.lower().strip().replace(".", ""), item.split(';'))))
        return KeywordItem(name=result)
