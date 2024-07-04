"""Database File to Store Scrapped Data"""

from sqlite3 import connect, ProgrammingError, OperationalError
from utils import SqlExecutionError
from constant import DB, SQL_EXECUTION_ERROR, CREATE_TABLE, INSERT_2_TABLE


class WeatherDatabase:
    """Weather Database to Handle Data"""

    def __init__(self):
        """Constructor for WeatherDatabase.__main__ class"""
        self.db = connect(DB)
        self.cursor = self.db.cursor()
        self.create_weather_table()

    def create_weather_table(self) -> None:
        """
        method to create table for Storing the Weather Data
        @return: None
        """
        try:
            self.cursor.execute(CREATE_TABLE)
            self.db.commit()
        except (ProgrammingError, OperationalError) as sql_error:
            print(SqlExecutionError(SQL_EXECUTION_ERROR.format(err=sql_error)))
            return

    def insert_into_city_table(self, weather_data: dict) -> None:
        """
        insert Weather data into database
        @param weather_data: dict
        @return: None
        """
        try:
            self.cursor.execute(INSERT_2_TABLE, weather_data)
            self.db.commit()
            print("Data Insertion Completed Check Database Table")
        except (ProgrammingError, OperationalError) as sql_error:
            print(SqlExecutionError(SQL_EXECUTION_ERROR.format(err=sql_error)))
            return
