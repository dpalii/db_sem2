import scrapy


class OdisseySpider(scrapy.Spider):
    name = "odissey"
    fields = {
        'link_pagination': '//ul[@class="pagination"]//a/@href',
        'link_category': '//div[contains(concat(" ",normalize-space(@class)," ")," catalog ")]//a/@href',
        'product': '//div[@class="panel-body"]//div[contains(concat(" ",normalize-space(@class)," ")," table-row ")]',
        'price': './/div[@class="pprice"]/text()',
        'name': './/a[@class="pnameh"]/text()',
        'img': './/img[@class="thumbnail"]/@src',
        'product_link': './/a[@class="pnameh"]/@href'
    }
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 0,
        'CLOSESPIDER_ITEMCOUNT': 20
    }
    start_urls = [
         'https://odissey.kiev.ua'
    ]
    allowed_domains = [
        'odissey.kiev.ua'
    ]

    def parse(self, response):
        for product in response.xpath(self.fields["product"]):
            yield {
                'link': product.xpath(self.fields['product_link']).extract(),
                'price': product.xpath(self.fields['price']).get().strip(),
                'img': map(lambda imgUrl: 'https://odissey.kiev.ua/' + imgUrl, product.xpath(self.fields['img']).extract()),
                'name': ''.join(product.xpath(self.fields['name']).extract())
            }
        for a in response.xpath(self.fields["link_category"]):
            yield response.follow(a.extract(), callback=self.parse)
        for a in response.xpath(self.fields["link_pagination"]):
            yield response.follow(a.extract(), callback=self.parse)
