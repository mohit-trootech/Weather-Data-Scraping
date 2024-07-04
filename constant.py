"""Constant Variables"""

# Required
URL = "https://www.timeanddate.com/weather/India/{city}"
DB = "WeatherDB.db"
# Errors
STATUS_CODE_ERROR = "Not Able to Fetch URL Return with Status Code: {status_code}"
SQL_EXECUTION_ERROR = "SQL Execution Failed Check Status: {err}"
BS4_ERROR = "Unable to Find Required Data Please Try Again or Check the Implementation"

# SQL Execution
CREATE_TABLE = (
    "CREATE TABLE IF NOT EXISTS temperature_data (id INTEGER PRIMARY KEY, city VARCHAR(64), city_query VARCHAR(32), "
    "temperature_info VARCHAR(1024), time_checked VARCHAR(64), last_updated VARCHAR(32), visibility VARCHAR(32), "
    "pressure VARCHAR(32),"
    "humidity INT);"
)

INSERT_2_TABLE = (
    "INSERT INTO temperature_data (city, city_query, temperature_info , time_checked, last_updated, visibility, "
    "pressure, humidity) VALUES (:city, :city_query, :temperature_info, :time_checked, :last_updated, :visibility, "
    ":pressure, :humidity);"
)
