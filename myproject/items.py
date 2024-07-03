# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class Headline(Item):
    title = Field()
    body = Field()

class Restaurant(Item):
    name = Field()
    address = Field()
    latitude = Field()
    longitude = Field()
    station = Field()
    store = Field()