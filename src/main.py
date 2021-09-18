# For a mapping of terms to max prices, search shopgoodwill.com for each term
# and send an email for each listing that is within the notifcation bounds and
# below its maximum price.
import smtplib
from bs4.element import PageElement
import requests
from urllib.parse import quote
import time
import os
import pytz

from goodwillproduct import GoodWillProduct
from goodwillsearch import GoodWillSearch





def main():
    SGW_TIMEZONE = pytz.timezone('America/Chicago')
    search = GoodWillSearch(SGW_TIMEZONE)
    
    products = {
    "rack mount",
    "wyze",
    "tiffany",
    "google home hub",
    "ryzen",
    "amd",
    "radeon"
}

    results = search.search_multiple(products)

    for result in results:
        result.print_product()




if __name__ == '__main__':
    main()