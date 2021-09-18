from bs4.element import PageElement
from unidecode import unidecode
from datetime import datetime
from datetime import timedelta
from bs4.element import PageElement
from urllib.parse import quote
import time
import os
import pytz
from unidecode import unidecode
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta 


class GoodWillProduct:
    def __init__(self, product: PageElement, time_zone: pytz.timezone):
        self.time_zone = time_zone
        self.html_product = product
        self.parse_product(product)       

    def time_zone(self):
        return self.time_zone

    def price(self):
        return self.price

    def listing(self):
        return self.listing
    
    def url(self):
        return self.url

    def product_id(self):
        return self.product_id

    def ends(self):
        return self.listing

    def end_date(self):
        return self.end_date

    def durration(self): 
        return self.durration

    def html_product(self):
        return self.html_product

    def print_product(self):
        print('price {} - listing: {} - url: {} durration: {}'.format(self.price, self.listing,self.url, self.durration))

    def parse_product(self, product: PageElement):
        self.price = product.find('div', {'class' : 'price' }).text.split(' ')[0].strip()[1:]
        self.price = float(self.price.replace(',', ''))
        self.listing = product.find('div', {'class' : 'title' }).text.strip().split('\n')[0].strip()
        self.product_id = product.find('div', {'class' : 'product-number' }).text.split(' ')[2]
        self.url = 'https://www.shopgoodwill.com/Item/{}'.format(self.product_id)

        if product.find('div.timer.countdown-classic.product-countdown'):
            self.ends = product.select('div.timer.countdown-classic.product-countdown')[0]['data-countdown']
            self.end_date = self.time_zone.localize(datetime.strptime(self.ends, '%m/%d/%Y %I:%M:%S %p'))
            self.durration = self.end_date - datetime.now(self.time_zone)
            self.durration = self.durration.total_seconds()
        else:
            self.end_date = datetime.now(self.time_zone)
            self.durration = 0

        self.listing = unidecode(self.listing)
