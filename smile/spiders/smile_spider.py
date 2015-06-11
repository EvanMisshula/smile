import scrapy
from smile.items import SmileItem

class smileSpider(scrapy.Spider):
    name = "smile"
    allowed_domains = [ "nytimes.com"]
    start_urls = [ "http://www.nytimes.com"]

    def parse(self, response):
        for idx, val in enumerate(response.css('img').xpath('@src')):
            key_item ="imageURL" + "-" + str(idx)
            print("the index is %d" % idx)
            print("the url selection is %s" % val)
            print("the item key is %s" % key_item)
            item = SmileItem()            
            item["imageURL"] = val.extract()
            item["keyItem"] = key_item
            yield item
