"""File to Implement Scraping data Class"""

import requests.models
from bs4 import BeautifulSoup
from constant import BS4_ERROR, CSV_OK
from database import WeatherDatabase
from utils import clean_format_data, Bs4Error
from weather_csv import CsvScrap


class DataScrap(WeatherDatabase):
    """DataScrap Class to Implement Scraping Inherits WeatherDatabase to Access Database"""

    def __init__(self, page, city_query: str) -> None:
        """
        Constructor for DataScrap.__main__ class
        @param city_query: str
        @param page: any
        """
        super().__init__()
        self.page = page
        self.city_query = city_query
        self.weather_data = None
        self.csv_object = CsvScrap()

    def scrap_filter_data(self) -> dict:
        """
        as the name suggest main method to implement data scraping and cleaning using utils and find.
        @return: dict
        """
        soup = BeautifulSoup(self.page.content, "html5lib")
        now = soup.find("div", {"id": "qlook"})
        tags = soup.find_all("td")
        if now and tags:
            self.weather_data = clean_format_data(self.city_query, now.text, tags)
            self.create_database_entry_of_scrap_data()
        else:
            raise Bs4Error(BS4_ERROR)

    def create_database_entry_of_scrap_data(self):
        self.insert_into_city_table(self.weather_data)

    def csv_handling(self, read: bool = False) -> None:
        """
        method to handle csv write and read operations
        @param: read: bool
        @return: None
        """
        self.csv_object.insert_into_csv(self.weather_data)
        print(CSV_OK)
        if read:
            self.csv_object.read_csv()
