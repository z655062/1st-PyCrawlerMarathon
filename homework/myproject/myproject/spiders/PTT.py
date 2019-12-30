# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class PttSpider(scrapy.Spider):
    name = 'PTT'
    allowed_domains = ['https://www.ptt.cc/bbs/Gossiping/M.1577684775.A.D8D.html']
    start_urls = ['http://www.ptt.cc/bbs/Gossiping/M.1577684775.A.D8D.html']

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        print(soup)
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, cookies={'over18': '1'})