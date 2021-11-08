import scrapy
import pandas as pd
import requests

class Scratch(scrapy.Spider):
    name = 'scratch'
    base = 'https://br.indeed.com/'
    start_urls = ['https://br.indeed.com/']
    domainGroups = []
    regularLinks = []
    endpoints = []
    linksWithParameters = []
    visitedEndpoints = []

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
        print("Doing my thing on: " + url)
        link = url.split('.com/')

        if(len(link) > 1):
            r = requests.get(self.base + link[1])
            linkStr = pd.Series([link[1]])

            has_slashes = linkStr.str.contains('/', regex=False)
            has_parameter = linkStr.str.contains('?', regex=False)

            if(has_slashes):
                self.treatLinkWithSlashes(linkStr)

            #>>>>>>>>>>>>>>>>>>>>>>>>>

            if (r.status_code == 200) and self.base + link[1] not in self.visitedEndpoints:
                self.endpoints.append(self.base + link[1])

                if (has_parameter[0]) and self.base + link[1] not in self.visitedEndpoints:
                    self.linksWithParameters.append(self.base + link[1])

    def printAll(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(self.endpoints)
        print(len(self.endpoints))

    def treatLinkWithSlashes(self, link):
        has_slashes = link.str.contains('/', regex=False)

        if(has_slashes):
            domain = link.split('/')
            self.domainGroups.append(self.base + domain[0])
            return self.treatLinkWithSlashes(domain[1])

        return link









