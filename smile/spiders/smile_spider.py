import scrapy
from smile.items import SmileItem

class smileSpider(scrapy.Spider):
    name = "smile"
    allowed_domains = [ "nytimes.com"]
    start_urls = [ "http://www.nytimes.com"]

    def parse(self, response):
        for sel in response.css('img').xpath('@src'):
#            index = response.css('img').xpath('@src').index(sel)
            item = SmileItem()
 #           key_item ="imageURL" + "-" + str(index)
            item["imageURL"] = sel.extract()
            yield item
