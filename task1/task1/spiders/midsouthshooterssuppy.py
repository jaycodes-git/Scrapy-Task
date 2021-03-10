import scrapy
from ..items import Task1Item   #Getproxies


class Spidera(scrapy.Spider):
    name = 'taskAspider'
    allowed_domains = ['www.midsouthshooterssupply.com']
    start_urls = ['https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1',
                  'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=2',
                  ]

    def parse(self, response, **kwargs):

        items = Task1Item()

        for i in range(0, 30):
            name = response.css('.catalog-item-name::text')[i].extract()
            price = response.css('.price span::text')[i].extract().replace('$', '')
            price = float(price)
            manf = response.css('.catalog-item-brand::text')[i].extract()
            instock = response.css('.out-of-stock::text')[i].extract()
            if instock == 'In Stock':
                instock = True
            else:
                instock = False

            items['name'] = name
            items['price'] = price
            items['manf'] = manf
            items['instock'] = instock

            yield items


# class ProxySpider(scrapy.Spider):
#     name = 'proxyspider'
#     allowed_domains = ['http://www.freeproxylists.net/']
#     start_urls = ['http://www.freeproxylists.net/',
#                   ]
#
#     def parse(self, response, **kwargs):
#         proxies = Getproxies()
#
#         proxy = response.css('.Even a , .Odd td:nth-child(1)').extract()
#
#         proxies['proxy'] = proxy
#
#         yield proxies