# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()
    comments = scrapy.Field()


class PersonInfoItem(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()
    salary = scrapy.Field()
    phone = scrapy.Field()


class BlogItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    post_time = scrapy.Field()
    category = scrapy.Field()
    detail = scrapy.Field()
