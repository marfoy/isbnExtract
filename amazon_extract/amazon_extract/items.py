# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonExtractItem(scrapy.Item):
	title = scrapy.Field()
	autor = scrapy.Field()
	pages = scrapy.Field()
	isbn = scrapy.Field()
	pass
