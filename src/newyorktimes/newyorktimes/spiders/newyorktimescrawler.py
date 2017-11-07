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
    rules = (Rule(LinkExtractor(allow=[r'\d{4}/\d{2}/\d{2}/[a-z]+/[a-z]+/[^/]+']), callback="parse_item", follow=True),)
    def parse_item(self, response):
        self.log("Scraping: " + response.url)

        item = NewyorktimesItem()
        item['url'] = response.url

        f = open('articles/%d'%(self.idx), 'w', encoding='utf8')
        f.write(response.text)
        f.close()
        self.idx+=1
        return item