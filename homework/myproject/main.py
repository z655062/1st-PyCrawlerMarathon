import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    #target_urls = [
    #    'http://www.ptt.cc/bbs/Gossiping/M.1577687305.A.E7E.html'
    #]
    boards = [
        'Gossiping'
#        'NBA'
    ]
    process = CrawlerProcess(get_project_settings())
    for board in boards:
        process.crawl('PTT', board=board)
    process.start()

if __name__ == '__main__':
    main()
