import scrapy
from myproject.items import Headline

class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["news.yahoo.co.jp"]
    start_urls = ["https://news.yahoo.co.jp"]

    def parse(self, response):
        res = response.css('section#uamods-topics')
        res_url = res.css('ul a::attr("href")').getall()

        for url in res_url:
            yield response.follow(url, self.parse_topics)

    def parse_topics(self, response):
        item = Headline()
        item['title'] = response.css('.sc-gdv5m1-1.hrYwtd::text').get()
        item['body'] = response.css('.sc-gdv5m1-7.jzYyxA.highLightSearchTarget::text').get()
        yield item