# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MyprojectPipeline(object):
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
    def open_spider(self, spider):
        print('開始!!')
        self.file = open('test.txt', 'w')
    def close_spider(self, spider):
        self.file.close()
        print('結束!!!')