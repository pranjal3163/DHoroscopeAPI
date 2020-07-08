# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
from main.models import HoroscopeItem
from pydispatch import dispatcher
from scrapy import signals
import json

class ScrapyDhoroscopePipeline:
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'),
        )

    def process_item(self, item, spider):
        scrapy_item = HoroscopeItem()
        # convert the  current date from string to DateTimeField
        str_date= item['current_date']
        date_formated = datetime.strptime(str_date, '%B %d, %Y')
        scrapy_item.unique_id = self.unique_id
        scrapy_item.sign_name = item['sign_name']
        scrapy_item.date_range = item['date_range']
        scrapy_item.current_date = date_formated.strftime('%Y-%m-%d')
        scrapy_item.description = item['description']
        scrapy_item.compatibility = item['compatibility']
        scrapy_item.mood = item['mood']
        scrapy_item.color = item['color']
        scrapy_item.lucky_number = item['lucky_number']
        scrapy_item.lucky_time = item['lucky_time']
        scrapy_item.save()
        return item

    def spider_closed(self, spider):
        print('SPIDER FINISHED!')