# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from myproject.items import MyprojectItem as Item

class PttSpider(scrapy.Spider):
    name = 'PTT'
    allowed_domains = ['https://www.ptt.cc/bbs/Gossiping/M.1577687305.A.E7E.html']
    start_urls = ['http://www.ptt.cc/bbs/Gossiping/M.1577687305.A.E7E.html']

    def parse(self, response):
        item = response.css('span[class="article-meta-value"]::text').extract()
        createItem = Item()
        createItem['author'] = item[0]
        createItem['plate'] = item[1]
        createItem['title'] = item[2]
        createItem['creatTime'] = item[3]
        return createItem
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, cookies={'over18': '1'})