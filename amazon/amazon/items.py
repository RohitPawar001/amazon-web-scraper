# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class MobileItem(scrapy.Item):
    title = scrapy.Field()
    brand = scrapy.Field()
    os = scrapy.Field()
    memory_size = scrapy.Field()
    screen_size = scrapy.Field()
    screen_resolution = scrapy.Field()
    price = scrapy.Field()
    discount = scrapy.Field()
    price_without_discount = scrapy.Field()
    star_rating = scrapy.Field()
    num_ratings = scrapy.Field()
    availibility = scrapy.Field()