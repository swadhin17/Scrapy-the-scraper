# -*- coding: utf-8 -*-
import scrapy

class Test2Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['acm.timus.ru']
    start_urls = ['http://acm.timus.ru/ranklist.aspx']

    def parse(self, response):
        users = response.xpath("//*[@class='content']")
        for user in users:
            country = user.xpath(".//td/div[starts-with(@class , 'flags-img')]/@title").extract()
            rank = user.xpath(".//td/text()").extract_first()
            author = user.xpath(".//td/a/text()").extract()
            rating = user.xpath(".//td[last()-2]/text()").extract()
            solved = user.xpath(".//td[last()-1]/text()").extract()
#            print(country , rank , author , solved , rating)
            yield{
                  'rank':rank ,
                  'country': country,
                  'author': author,
                  'rating' : rating , 
                  'solved': solved
              }
            
        next_page= response.xpath("//td[@class='ranklist_footer_right']/nobr/a/@href").extract()[1]

        if next_page is not None:
            next_page_link= response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)    
