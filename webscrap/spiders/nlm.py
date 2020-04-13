# -*- coding: utf-8 -*-
import scrapy
from webscrap.items import KeywordItem
import urllib.parse
import os


class NlmSpider(scrapy.Spider):
    name = 'nlm'
    allowed_domains = ['www.ncbi.nlm.nih.gov']

    def start_requests(self):
        url = 'https://www.ncbi.nlm.nih.gov/pubmed/'
        tag = os.environ['AUTHOR']
        if tag is not None:
            url = url + '?term=' + urllib.parse.quote(tag) + '%5BAuthor%5D+&EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.PageSize=200'
        self.logger.info("new url "+ url)
        yield scrapy.Request(url, self.parse)


    def parse(self, response):
        for link in response.xpath('//*[@id="maincontent"]/div/div[5]/div[@class="rprt"]/div[@class="rslt"]/p/a/@href').getall():
            extracted_link = response.urljoin(link)
            self.logger.info("execute link " + extracted_link)
            yield scrapy.Request(extracted_link, self.parse_sub_link)

    def parse_sub_link(self, response):
        keyword = response.xpath('//*[@id="maincontent"]/div/div[@class="rprt_all"]/div/div[@class="keywords"]/p/text()').get()
        if keyword:
            self.logger.info("Received keyword " + keyword)
            res_list = list(map(lambda x: x.lower().strip(), keyword.split(';')))
            return KeywordItem(name=res_list)

