import scrapy


class MlSpider(scrapy.Spider):
    name = "ml"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/fralda"]

    def parse(self, response):
        pass
