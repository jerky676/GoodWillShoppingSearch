from datetime import datetime
from urllib import parse
from queryitem import QueryItem
from goodwillsearchgallery import GoodWillSearchGallery
from goodwillcategories import GoodWillCategories
from goodwilllocations import GoodWillLocations
from goodwillproduct import GoodWillProduct
from urllib.parse import quote
import pytz
from bs4.element import PageElement
from bs4 import BeautifulSoup
import requests

class GoodWillSearch:
    def __init__(self, time_zone: pytz.timezone):
        self.time_zone = time_zone
        self.url = "https://www.shopgoodwill.com/Listings"
        self.search_gallery = QueryItem("sg",GoodWillSearchGallery.Empty)    
        self.keyword_search = QueryItem("st","")
        self.categories = QueryItem("c","")
        self.good_will_location = QueryItem("s","")
        self.low_price = QueryItem("lp",0)
        self.high_price = QueryItem("hp",999999)
        self.show_buy_now_only = QueryItem("sbn",False)
        self.show_pick_up_only = QueryItem("spo",False)
        self.hide_pick_up_only = QueryItem("snpo",False)
        self.show_one_cent_ship_only = QueryItem("socs",False)
        self.search_description = QueryItem("sd",True)
        self.show_closed_auctions = QueryItem("sca",False)
        self.closed_auction_end_date = QueryItem("caed",'11/14/2018')
        self.day_back = QueryItem("cadb",9)
        self.search_canada = QueryItem("scs",False)
        self.search_international = QueryItem("sis",False)
        self.field_order = QueryItem("col",0)
        self.page_number = QueryItem("p",0)
        self.page_size = QueryItem("ps",40)
        self.short_description = QueryItem("desc",True)
        self.saved_search_id = QueryItem("ss",0)
        self.use_buyer_prefrences = QueryItem("UseBuyerPrefs",True)       

    def search(self,keyword_search:str):
        self.keyword_search_set(quote(keyword_search))
        return self.parse_results(requests.get(self.search_url()).text)

    def search_multiple(self,keyword_search:set[str]):
        goodWillProducts = [GoodWillProduct]
        for keyword in keyword_search:
            goodWillProducts.extend(self.search(keyword))

        return goodWillProducts

    def parse_results(self, response):
        goodWillProducts = [GoodWillProduct]
        soup = BeautifulSoup(response, 'html.parser')
        products = soup.find_all('span', {'class' : 'data-container'})
        for product in products:
            goodWillProduct = GoodWillProduct(product,self.time_zone)
            goodWillProduct.print_product()
            goodWillProducts.append(goodWillProduct)
        
        return goodWillProducts

    def query_string (self):
        query_string = "?"
        for attrib, value in self.__dict__.items():
            if type(value) is QueryItem:
                query_string += f'{value.query_string_value()}&'

        return query_string

    def search_url(self):
        return self.url + self.query_string()

    def search_gallery(self):
        return self.search_gallery.value()

    def search_gallery(self, value: GoodWillSearchGallery):
        self.search_gallery.value_set(value)

    def keyword_search(self):
        return self.keyword_search.value()

    def keyword_search_set(self, value: str):
        self.keyword_search.value_set(value)

    def categories(self):
        return self.categories.value()

    def categories_set(self, value: GoodWillCategories):
        self.categories.value_set(value)

    def good_will_location(self):
	    return self.good_will_location.value()

    def good_will_location(self, value:GoodWillLocations):
        self.good_will_location.value_set(value)

    def closed_auction_date(self):
        return self.search_gallery.value()

    def closed_auction_date(self, closed_auction_date: datetime):
        self.search_gallery = closed_auction_date

    def low_price(self):
        return self.low_price.value()

    def low_price(self, value:int):
        self.low_price.value_set(value)

    def high_price(self):
        return self.high_price.value()

    def high_price(self, value:int):
        self.high_price.value_set(value)

    def show_buy_now_only(self):
        return self.show_buy_now_only

    def show_buy_now_only(self, value:bool):
        self.show_buy_now_only.value_set(value)

    def show_pick_up_only(self):
        return self.show_pick_up_only.value

    def show_pick_up_only(self, value:bool):
        self.show_pick_up_only.value_set(value)

    def hide_pick_up_only(self):
        return self.hide_pick_up_only.value()

    def hide_pick_up_only(self, value:bool):
        self.hide_pick_up_only.value_set(value)

    def show_one_cent_ship_only(self):
        return self.show_one_cent_ship_only.value()

    def show_one_cent_ship_only(self, value:bool):
        self.show_one_cent_ship_only.value_set(value)

    def search_description(self):
        return self.search_description.value()

    def search_description(self, value:bool):
        self.search_description.value_set(value)

    def show_closed_auctions(self):
        return self.show_closed_auctions.value()

    def show_closed_auctions(self, value:bool):
        self.show_closed_auctions.value_set(value)

    def closed_auction_end_date(self):
        return self.closed_auction_end_date.value()

    def closed_auction_end_date(self, value:datetime):
        self.closed_auction_end_date.value_set(value)

    def day_back(self):
        return self.day_back.value()

    def day_back(self, value:int):
        self.day_back.value_set(value)

    def search_canada(self):
        return self.search_canada.value()

    def search_canada(self, value:bool):
        self.search_canada.value_set(value)

    def search_international(self):
        return self.search_international.value()

    def search_international(self, value:bool):
        self.search_international.value_set(value)

    def page_number(self):
        return self.page_number.value()

    def page_number(self, value:int):
        self.page_number.value_set(value)

    def page_size(self):
        return self.page_size.value()

    def page_size(self, value:int):
        self.page_size.value_set(value)

    def short_description(self):
        return self.short_description.value()

    def short_description(self, value:bool):
        self.short_description.value_set(value)

    def saved_search_id(self):
        return self.saved_search_id.value()

    def saved_search_id(self, value:int):
        self.saved_search_id.value_set(value)

    def use_buyer_prefrences(self):
        return self.use_buyer_prefrences.value()

    def use_buyer_prefrences(self, value:bool):
        self.use_buyer_prefrences.value_set(value)
