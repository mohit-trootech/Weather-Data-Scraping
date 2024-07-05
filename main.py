"""Python Scrapping Project using BS4, Requests, html5lib Library
JustDial: Query Based Scrapping using sqlite Database to Store Data and CSV File for Better Data Understanding"""

from requests import get
from constant import STATUS_CODE_ERROR, STATUS_CODE_OK
from scraping import DataScrap
from utils import get_request_url, RequestError


def main() -> None:
    """
    driver Code Class
    @return:
    """
    print("Welcome to Scraping Project Please Enter Country Code and City Name")
    city = input("Enter City Name: ")
    page = get(get_request_url(city))
    if page.status_code == STATUS_CODE_OK:
        scrap_obj = DataScrap(page, city)
        scrap_obj.scrap_filter_data()
    else:
        raise RequestError(STATUS_CODE_ERROR.format(status_code=page.status_code))
    write = input("Enter Y to Write CSV: ")
    read = input("Enter Y to Read CSV: ")
    if write.lower() == "y":
        if read.lower() == "y":
            scrap_obj.csv_handling(read=True)
        else:
            scrap_obj.csv_handling()


if __name__ == "__main__":
    main()
