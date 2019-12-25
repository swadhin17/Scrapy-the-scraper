# -*- coding: utf-8 -*-
import scrapy


class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['codeforces.com']
    start_urls = ['https://codeforces.com/ratings/page/1']

    def parse(self, response):
#        
# =============================final1================================================
#         users1 = response.xpath("//div[@class='datatable ratingsDatatable']/div[@style='background-color: white;margin:0.3em 3px 0 3px;position:relative;']/table/tr/td/a")
#         for user in users1:
#             first = user.xpath(".//span/text()").extract()
#             second = user.xpath(".//text()").extract()
#             if (len(first)!=1):
#                 user = second[0]
# #                print(user)
#             else:
#                 user = first[0] + second[1]
# #                print(user)
#                 
#             yield{
#                  'user': user   
#                 }    
#==========================================final2===================================
        users = response.xpath("//div[@class='datatable ratingsDatatable']/div[@style='background-color: white;margin:0.3em 3px 0 3px;position:relative;']/table/tr")
        for user1 in users:
            rate = user1.xpath(".//td[last()]/text()").extract()
            country = user1.xpath(".//td/img/@alt").extract()
            num_participated = user1.xpath(".//td[last()-1]/text()").extract()
            
            yield{
                     'rate':rate,
                     'num_participated':num_participated,
                     'country':country
                     
                     }
             
#=============================================================================

        