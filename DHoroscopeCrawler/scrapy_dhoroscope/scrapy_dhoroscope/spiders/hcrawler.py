# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.spiders import CrawlSpider

from .. import items

from bs4 import BeautifulSoup


class hcrawler(CrawlSpider):
    name = 'hcrawler'

    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.day = kwargs.get('day')
        self.allowed_domains = [self.domain]
        self.category_dict = {
            'Capricorn': 1,
            'Aquarius': 2,
            'Pisces':3,
            'Aries': 4,
            'Taurus': 5,
            'Gemini': 6,
            'Cancer': 7,
            'Leo': 8,
            'Virgo': 9,
            'Libra': 10,
            'Scorpio': 11,
            'Sagittarius': 12
        }

    def start_requests(self):
        days = {"yesterday","today","tomorrow"}
        urls = [
            'http://astrology.kudosmedia.net/m/capricorn?day=',
            'http://astrology.kudosmedia.net/m/aquarius?day=',
            'http://astrology.kudosmedia.net/m/pisces?day=',
            'http://astrology.kudosmedia.net/m/aries?day=',
            'http://astrology.kudosmedia.net/m/taurus?day=',
            'http://astrology.kudosmedia.net/m/gemini?day=',
            'http://astrology.kudosmedia.net/m/cancer?day=',
            'http://astrology.kudosmedia.net/m/leo?day=',
            'http://astrology.kudosmedia.net/m/virgo?day=',
            'http://astrology.kudosmedia.net/m/libra?day=',
            'http://astrology.kudosmedia.net/m/scorpio?day=',
            'http://astrology.kudosmedia.net/m/sagittarius?day='
        ]
        for url in urls:
            for day in days:  # Sunshine by day
                yield scrapy.Request(url= url + day, callback=self.parse_sunshine)

    def parse_sunshine(self, response):  # Get all sunshine details

        soup = BeautifulSoup(str(response.body), 'lxml')

        sign_name = str(soup.find("td", {"style": "vertical-align:middle;"}).text) \
            .partition("\\n\\t\\t\\t\\t\\t")[2] \
            .partition("\\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t")[0]

        date_range = str(soup.find("td", {"style": "vertical-align:middle;"}).text) \
            .partition("\\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t")[2] \
            .partition("\\t\\t\\t\\t")[0]

        current_date = soup.find(
            "p", {"style": "font-weight: bold; color: #336699;"}) \
            .text.partition(":")[2].replace("\\t", "")

        description = soup.find("p", {"style": "color: #333333;"}).text.replace("\\", "")

        details = soup.find(
            "ul",
            {"style": "margin: 0pt; padding: 0px; list-style-type: none;"
                      " list-style-image: none; list-style-position: outside;"
                      " color: #336699; font-size: 0.9em; "}).find_all("li")

        compatibility = details[0].text.partition(":")[2].strip()
        mood = details[1].text.partition(":")[2].strip()
        color = details[2].text.partition(":")[2].strip()
        lucky_number = details[3].text.partition(":")[2].strip()
        lucky_time = details[4].text.partition(":")[2].strip()


        item = items.ScrapyDhoroscopeItem()
        item['sign_name'] = str(sign_name)
        item['date_range'] = str(date_range)
        item['current_date'] = str(current_date)
        item['description'] = str(description)
        item['compatibility'] = str(compatibility)
        item['mood'] = str(mood)
        item['color'] = str(color)
        item['lucky_number'] = str(lucky_number)
        item['lucky_time'] = str(lucky_time)


        yield item