import scrapy

def start_requests(url):

    print(url)
    tt = scrapy.Request(url=url, callback=parse)
    print(tt.callback)

# urls = [
#     'https://br.indeed.com',
# ]
#
# for url in urls:
#
#     yield scrapy.Request(url=url, callback=self.parse)

def parse(self, response):
    print("works 2")
# for quote in response.xpath('//a[contains(@href, "*")]'):
#     link = quote.css('a::attr(href)').getall()


    # if link[0] not in self.urls:
    #
    #     find_exception = False
    #     for exception in self.exceptions:
    #         if link[0].find(exception, 0, 20) >= 0:
    #             find_exception = True
    #
    #     if not find_exception:
    #         self.urls.append(link[0])
    #
    #         yield {
    #             'article': link[0]
    #         }

    # yield {
    #     'article': quote.css('a::attr(href)').getall(),
    # }

    # next_page = response.css('li.next a::attr(href)').get()
    # if next_page is not None:
    #     next_page = response.urljoin(next_page)
    #     yield scrapy.Request(next_page, callback=self.parse)



start_requests('https://br.indeed.com')

