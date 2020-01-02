import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_urls = [
        'http://www.ptt.cc/bbs/Gossiping/M.1577687305.A.E7E.html'
    ]
    process = CrawlerProcess(get_project_settings())
    process.crawl('PTT', start_urls=target_urls, filename='test.json')
    process.start()

if __name__ == '__main__':
    main()
