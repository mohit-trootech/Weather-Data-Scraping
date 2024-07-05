"""Weather Scrap Data CSV Update"""

import os
from csv import writer, reader
from constant import CSV_PATH, CSV_NOT_FOUND
from utils import CsvFileNotExists


class CsvScrap:
    """class to implement csv logic for scraping"""

    def __init__(self):
        if not os.path.isfile(CSV_PATH):
            with open("weather.csv", "a") as fp:
                data = (
                    "city",
                    "city_query",
                    "temperature_info",
                    "time_checked",
                    "last_updated",
                    "visibility",
                    "pressure",
                    "humidity",
                )
                write_obj = writer(fp)
                write_obj.writerow(data)

    @staticmethod
    def insert_into_csv(weather_data: dict) -> None:
        """
        static method just to write a CSV File
        @param weather_data: dict
        @return:None
        """
        if os.path.isfile(CSV_PATH):
            with open("weather.csv", "a") as fp:
                data = weather_data.values()
                write_obj = writer(fp)
                write_obj.writerow(data)
        else:
            raise CsvFileNotExists(CSV_NOT_FOUND)

    @staticmethod
    def read_csv() -> None:
        """
        static method just to read a CSV File
        @return:None
        """
        if os.path.isfile(CSV_PATH):
            with open("weather.csv", "r") as fp:
                read = reader(fp)
                for row in read:
                    print(row)
        else:
            raise CsvFileNotExists(CSV_NOT_FOUND)


if __name__ == "__main__":
    obj = CsvScrap()
    obj.read_csv()
