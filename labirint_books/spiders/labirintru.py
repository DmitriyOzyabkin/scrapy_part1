import scrapy
from scrapy.http import HtmlResponse
from items import LabirintBooksItem


class LabirintruSpider(scrapy.Spider):
    name = "labirintru"
    allowed_domains = ["labirint.ru"]
    start_urls = ["https://www.labirint.ru/genres/2791/?page=1"]

    def parse(self, response):

        # next_page = response.xpath("//a[@class='pagination-next__text']/@href").get()
        # if next_page:
        #     next_page = "https://www.labirint.ru/genres/2791/" + next_page
        #     yield response.follow(next_page, callback=self.parse)

        links = ["https://www.labirint.ru" + link for link in response.xpath("//div[contains(@class, 'genres-catalog')]//div[@class='genres-carousel__item']//div[@class='product-cover']/a/@href").getall()]
        for link in links:
            yield response.follow(link, callback=self.book_parse)
        
        
        
        
    def book_parse(self, response:HtmlResponse):

        id = response.xpath("//div[@class='articul']/text()").get()
        isbn = response.xpath("//div[@class='isbn']/text()").get()
        genre = response.xpath("//div[@class='genre']/a/text()").getall()
        title = response.xpath("//h1/text()").get()
        author = response.xpath("//div[@class='authors']/a/text()").getall()
        rate = response.xpath("//div[@id='rate']/text()").get()
        book_url = response.url

        yield LabirintBooksItem(id=id, isbn=isbn, genre=genre, title=title, author=author, rate=rate, book_url=book_url)
