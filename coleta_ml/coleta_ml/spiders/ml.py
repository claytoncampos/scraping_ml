import scrapy


class MlSpider(scrapy.Spider):
    name = "ml"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/fralda"]

    def parse(self, response):
        products = response.css('div.ui-search-result__content')

        for product in products:
            prices = product.css('span.andes-money-amount__fraction::text').getall()
            cents = product.css('span.andes-money-amount__cents::text').getall()
            
            yield {
                'brand' : product.css('h2.ui-search-item__title::text').get(),
                'name' : product.css('h2.ui-search-item__title::text').get(),
                'old_price_reais' : prices[0] if len(prices) > 0 else None,
                'old_price_centavos' : cents[0] if len(cents) > 0 else None,
                'new_price_reais' : prices[1] if len(prices) > 1 else None,
                'new_price_centavos' : cents[1] if len(cents) > 1  else None,
                'reviews_rating_number' : product.css('span.ui-search-reviews__rating-number::text').get(),
                'reviews_amount' : product.css('span.ui-search-reviews__amount::text').get()
            }
