# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from collections import Counter

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('/data/items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class BasicAggregatorPipeline(object):

    def open_spider(self, spider):
        self.file = open('/data/items.json', 'w')
        self.res = dict()

    def close_spider(self, spider):
        c = Counter(self.res)
        mc = {item[0]: item[1] for item in c.most_common(5)}
        print(mc)
        self.file.write(json.dumps(mc))
        self.file.close()

    def process_item(self, item, spider):
        for key in item['name']:
            if key in self.res:
                self.res[key] = self.res[key] + 1
            else:
                self.res[key] = 1
        return item