# -*- coding: utf-8 -*-
# to run type scrapy runspider news-translations.py -o output.csv
# add more websites
https://www.aps.dz/ar/algerie
https://www.aps.dz/
https://www.tsa-algerie.com/


import scrapy
from googletrans import Translator

translator = Translator()

class QuotesSpider(scrapy.Spider):
    name = 'tsa-arabic'
    start_urls = ['https://www.tsa-algerie.com/ar/']

    def parse(self, response):
        for quote in response.css('.title-middle a'):
            # works well, but too verbose
            # print ('header:', quote.css('::text').get())

            # send results to file
            yield {
                'header': translator.translate(quote.css('::text').get(), src='ar', dest='fr').text
            }
