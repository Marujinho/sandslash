import scrapy
import pandas as pd
import requests

#enter url
class Scratch(scrapy.Spider):
    name = 'scratch'
    base = 'https://br.indeed.com/'
    urls = []
    regularLinks = []
    endpoints = []
    linksWithParameters = []
    visitedEndpoints = []
    counter = 0

    def __init__(self):
        self.endpoints.append(self.base)

    def start_requests(self):
        #urls = self.endpoints

        for url in self.endpoints:
            if url not in self.visitedEndpoints:
                yield scrapy.Request(url=url, callback=self.parse)
                self.visitedEndpoints.append(url)

    def parse(self, response, **kwargs):
        links = response.css('a::attr(href)').getall()

        for link in links:
            self.filterUrl(link)

        self.printAll()

    def filterUrl(self, url):
        print("Doing my thing...")
        link = url.split('.com/')

        if(len(link) > 1):
            r = requests.get(self.base + link[1])
            str_1 = pd.Series([link[1]])
            has_parameter = str_1.str.contains('?', regex=False)

            if (r.status_code == 200):
                self.endpoints.append(self.base + link[1])

                if (has_parameter[0]):
                    self.linksWithParameters.append(self.base + link[1])


        return self.linksWithParameters

            #yield {'regularLink':link[0] }
            #print(self.endpoints)
            #yield {'withParameters':link[1] }

    def printAll(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(self.linksWithParameters)
        return self.start_requests()

#get all links
