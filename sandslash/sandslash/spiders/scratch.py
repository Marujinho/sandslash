import scrapy
import pandas as pd
import requests

class Scratch(scrapy.Spider):
    name = 'scratch'
    base = 'https://br.indeed.com/'
    start_urls = ['https://br.indeed.com/']
    urls = []
    regularLinks = []
    endpoints = []
    linksWithParameters = []
    visitedEndpoints = []
    counter = 0


    def parse(self, response, **kwargs):
        self.visitedEndpoints.append(response.request.url)
        links = response.css('a::attr(href)').getall()

        if (len(self.endpoints) > 0):
            self.endpoints.pop(0)

        for link in links:
            self.filterUrl(link)

        self.printAll()

        for url in self.endpoints:
            if url not in self.visitedEndpoints:
                self.visitedEndpoints.append(url)
                yield scrapy.Request(url=url, callback=self.parse)

    def filterUrl(self, url):
        print("Doing my thing...")
        link = url.split('.com/')

        if(len(link) > 1):
            r = requests.get(self.base + link[1])
            str_1 = pd.Series([link[1]])
            has_parameter = str_1.str.contains('?', regex=False)

            if (r.status_code == 200) and self.base + link[1] not in self.visitedEndpoints:
                self.endpoints.append(self.base + link[1])

                if (has_parameter[0]) and self.base + link[1] not in self.visitedEndpoints:
                    self.linksWithParameters.append(self.base + link[1])

    def printAll(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(self.endpoints)
        print(len(self.endpoints))




