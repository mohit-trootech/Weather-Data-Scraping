"""File to Implement Scrapping data Class"""

import requests.models
from bs4 import BeautifulSoup

from constant import BS4_ERROR
from database import WeatherDatabase
from utils import clean_format_data, Bs4Error


class DataScrap(WeatherDatabase):
    """DataScrap Class to Implement Scrapping Inherits WeatherDatabase to Access Database"""

    def __init__(self, page, city_query: str) -> None:
        """
        Constructor for DataScrap.__main__ class
        @param city_query: str
        @param page: any
        """
        super().__init__()
        self.page = page
        self.city_query = city_query

    def scrap_filter_data(self) -> dict:
        """
        as the name suggest main method to implement data scrapping and cleaning using utils and find.
        @return: dict
        """
        soup = BeautifulSoup(self.page.content, "html5lib")
        now = soup.find("div", {"id": "qlook"})
        tags = soup.find_all("td")
        if now and tags:
            weather_data = clean_format_data(self.city_query, now.text, tags)
            self.create_database_entry_of_scrap_data(weather_data)
        else:
            raise Bs4Error(BS4_ERROR)

    def create_database_entry_of_scrap_data(self, weather_data):
        self.insert_into_city_table(weather_data)
