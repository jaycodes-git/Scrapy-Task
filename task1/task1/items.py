# Define here the models for your scraped items

import scrapy


class Task1Item(scrapy.Item):
    
    name = scrapy.Field()
    price = scrapy.Field()
    manf = scrapy.Field()
    instock = scrapy.Field()
