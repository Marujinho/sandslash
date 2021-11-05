import scrapy
import pandas as pd

#enter url
class Scratch(scrapy.Spider):
    name = 'scratch'
    base = 'https://br.indeed.com/'
    urls = []
    regularLinks = []
    endpoints = []
    linksWithParameters = []

    def start_requests(self):
        urls = [
            'https://br.indeed.com/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        links = response.css('a::attr(href)').getall()

        for link in links:
            self.filterUrl(link)

        self.printAll()

    def filterUrl(self, url):
        link = url.split('.com/')

        if(len(link) > 1):
            #self.endpoints.append(link[1])

            str_1 = pd.Series([link[1]])
            has_parameter = str_1.str.contains('?', regex=False)

            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            # print(has_parameter[0])

            if has_parameter[0]:
                self.linksWithParameters.append(link[1])

            #yield {'regularLink':link[0] }
            #print(self.endpoints)
            #yield {'withParameters':link[1] }

    def printAll(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(self.linksWithParameters)

#get all links
