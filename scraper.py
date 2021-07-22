import requests

from bs4 import BeautifulSoup
from config import HEADERS


class Scraper(object):
    """Scraper Abstract class"""

    def __init__(self, url):
        """Default Scraper Constructor"""
        self.url = url
        self.html = ''
        self.soup = None
        self.price = ''

        self.get_html_from_url()
        self.get_parsed_bs4_from_html()

    def get_html_from_url(self):
        """
        Get html string from url
        :return: html: string
        """
        r = requests.get(self.url, headers=HEADERS)

        if r.status_code == 200:
            self.html = r.text.strip()
        return self.html

    def get_parsed_bs4_from_html(self, parser='lxml'):
        """
        Get parsed bs4object(soup) from html string
        :param parser: string
        :return: soup: bs4 Object
        """
        self.soup = BeautifulSoup(self.html, parser)
        return self.soup


class ZillowScraper(Scraper):
    """ZillowScraper Child class inherits from Scraper Parent"""

    def __init__(self, url):
        """Default ZillowScraper Constructor"""
        super().__init__(url)
        self.name = 'zillow'

    def run(self):
        """
        Get price from bs4 soup object
        :return: name, price
        """
        price_section = self.soup.find('div', class_='ds-bed-bath-living-area-header').find_previous('span')
        if price_section:
            self.price = price_section.text.strip()
        return self.name, self.price


class RedfinScraper(Scraper):
    """RedfinScraper Child class inherits from Scraper Parent"""

    def __init__(self, url):
        """Default RedfinScraper Constructor"""
        super().__init__(url)
        self.name = 'redfin'

    def run(self):
        """
        Get price from bs4 soup object
        :return: name, price
        """
        price_section = self.soup.find('div', class_='panel-title', text='Home Price').find_next('div')
        if price_section:
            self.price = price_section.text.strip()
        return self.name, self.price
