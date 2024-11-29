import scrapy
from scrapy.http import HtmlResponse
from items import LabirintBooksItem


class LabirintruSpider(scrapy.Spider):
    name = "labirintru"
    allowed_domains = ["labirint.ru"]
    start_urls = ["https://www.labirint.ru/genres/2791/?page=1"]

    def parse(self, response):

        # Получеие ссылок на книги с каждой странички в категории "Фантастика"

        # Поиск и парсинг следующей странички, если есть
        next_page = response.xpath("//a[@class='pagination-next__text']/@href").get()
        if next_page:
            next_page = "https://www.labirint.ru/genres/2791/" + next_page
            yield response.follow(next_page, callback=self.parse)

        # Парсинг персой странички в выбранной категории
        links = ["https://www.labirint.ru" + link for link in response.xpath("//div[contains(@class, 'genres-catalog')]//div[@class='genres-carousel__item']//div[@class='product-cover']/a/@href").getall()]
        for link in links:
            yield response.follow(link, callback=self.book_parse)
        
        
        
        
    def book_parse(self, response:HtmlResponse):

        # Получение данные о каждой книги

        id = response.xpath("//div[@class='articul']/text()").get()             # id книги в каталоге labirint.ru
        isbn = response.xpath("//div[@class='isbn']/text()").get()              # ISBN книги
        genre = response.xpath("//div[@class='genre']/a/text()").getall()       # Список категории жаров книги
        title = response.xpath("//h1/text()").get()                             # Название книги
        author = response.xpath("//div[@class='authors'][1]/a/text()").getall() # Список авторов
        rate = response.xpath("//div[@id='rate']/text()").get()                 # Рейтинг кнги на сайте
        book_url = response.url                                                 # Прямая ссылка на книгу

        yield LabirintBooksItem(id=id, isbn=isbn, genre=genre, title=title, author=author, rate=rate, book_url=book_url)
