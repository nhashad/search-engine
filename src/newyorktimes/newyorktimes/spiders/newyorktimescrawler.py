# -*- coding: utf-8 -*-
import scrapy
from newspaper import Article
from newyorktimes.items import NewyorktimesItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class NewyorktimescrawlerSpider(CrawlSpider):
    name = 'newyorktimescrawler'
    idx = 0
    allowed_domains = ['www.nytimes.com']
    start_urls = ['https://www.nytimes.com/section/world/europe']
    custom_settings = {
                       'CLOSESPIDER_ITEMCOUNT': 500,
                        'CONCURRENT_REQUESTS': 1
                       }
    
    rules = (Rule(LinkExtractor(allow=[r'\d{4}/\d{2}/\d{2}/[a-z]+/[a-z]+/[^/]+\.html']), callback="parse_item", follow=True),)
    def parse_item(self, response):
        self.log("Scraping: " + response.url)

        item = NewyorktimesItem()
        item['url'] = response.url
        article = Article(item['url'], language='en')
        article.download()
        article.parse()
        item['link_authors'] = ', '.join(article.authors)
        item['link_title'] = article.title
        text =  article.text
                
        file_name = '%d-%s'%(self.idx, item['link_title'])
        file_text = 'Author(s): %s\nurl: %s\n\n%s'%(item['link_authors'], item['url'], text)

        f = open('articles/%s.txt'%(file_name), 'w', encoding='utf8')
        f.write(file_text)
        f.close()
        self.idx+=1
        return item