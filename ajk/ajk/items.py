# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AjkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TEST_Item(scrapy.Item):
    # define the fields for your item here like:
    year= scrapy.Field()
    price=scrapy.Field()
    wbs=scrapy.Field()
    print("^^^^^^^^^^I have run ITems^^^^^^^^^")


