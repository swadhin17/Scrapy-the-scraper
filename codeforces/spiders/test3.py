# -*- coding: utf-8 -*-
import scrapy
import string 

class Test3Spider(scrapy.Spider):
    name = 'test3'
    allowed_domains = ['codeforces.com']
    start_urls = ['https://codeforces.com/problemset/standings/']

    def parse(self, response):
        users = response.xpath("//div[@class='datatable']/div/table/tr")
        for user in users:
#            country = user.xpath(".//td/div[starts-with(@class , 'flags-img')]/@title").extract()
            rank = user.xpath(".//td/text()").extract_first()
            author = user.xpath(".//td/a/text()").extract()
#            rating = user.xpath(".//td[last()-2]/text()").extract()
            solved = user.xpath(".//td[last()]/text()").extract()
            catagories = user.xpath(".//td/a/@title").extract()

            yield{
                  'rank':rank ,
#                  'country': country,
                  'author': author,
                  'catagory' : catagories , 
                  'solved': solved
              }
            
        r = response.xpath("//*[@class='page-index active']/a/following::node()")
        next_page =  "https://codeforces.com" + r.xpath(".//span/a/@href").extract_first()   
        if next_page is not None:
            next_page_link= response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)    


