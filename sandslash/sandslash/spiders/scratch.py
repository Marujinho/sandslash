import scrapy

#enter url
class Scratch(scrapy.Spider):
    name = 'scratch'
    urls = []
    endpoints = []

    def start_requests(self):
        urls = [
            'https://br.indeed.com/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        links = response.css('a::attr(href)').getall()

        for link in links:
            self.endpoints.append(link)

        print(self.endpoints)

        # for quote in response.xpath('//a[contains(@href, "*")]'):
        #     page = quote.css('a::attr(href)').getall()
        #
        #     if page[0] not in self.urls:
        #
        #         self.urls.append(page[0])
        #
        #         yield {
        #             'endpoint': page[0]
        #         }

#get all links
