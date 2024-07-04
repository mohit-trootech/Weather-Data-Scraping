"""Scrapping Utilities: geturl, get error message, etc"""

import re

from constant import URL


class CsvFileNotExists(BaseException):
    """Custom class for CSV File Not Found"""

    def __init__(self, msg):
        super(CsvFileNotExists, self).__init__(msg)


class SqlExecutionError(BaseException):
    """Custom class for SQL Exception"""

    def __init__(self, msg):
        super(SqlExecutionError, self).__init__(msg)


class RequestError(BaseException):
    """custom class for all request status code error other than 200"""

    def __init__(self, msg):
        super(RequestError, self).__init__(msg)


class Bs4Error(BaseException):
    """custom bs4 Exception class"""

    def __init__(self, msg):
        super(Bs4Error, self).__init__(msg)


def get_request_url(city: str = "Mumbai") -> str:
    """
    get Request URL City
    @param city: str
    @return: str
    """
    return URL.format(city=city)


def clean_format_data(city_query: str, now: str, tags: list) -> dict:
    """
    function to clean and get required data from scrapped data and create dictionary from it
    @param city_query:str
    @param now:str
    @param tags:list
    @return:dict
    """
    weather_data = {}
    info = [re.sub(r"\xa0", " ", tag.text) for tag in tags]
    weather_data.setdefault("temperature_info", re.sub(r"\xa0", " ", now))
    weather_data.update(
        {
            "city": info[0],
            "city_query": city_query,
            "time_checked": info[1],
            "last_updated": info[2],
            "visibility": info[3],
            "pressure": info[4],
            "humidity": info[5],
        }
    )
    return weather_data
