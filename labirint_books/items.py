# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LabirintBooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    isbn = scrapy.Field()
    genre = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    rate = scrapy.Field()
    book_url = scrapy.Field()
