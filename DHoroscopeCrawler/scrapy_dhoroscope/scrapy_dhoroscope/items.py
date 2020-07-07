# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDhoroscopeItem(scrapy.Item):
    unique_id = scrapy.Field()
    sign_name = scrapy.Field()
    date_range = scrapy.Field()
    current_date = scrapy.Field()
    description = scrapy.Field()
    compatibility = scrapy.Field()
    mood = scrapy.Field()
    color = scrapy.Field()
    lucky_number = scrapy.Field()
    lucky_time = scrapy.Field()
    pass