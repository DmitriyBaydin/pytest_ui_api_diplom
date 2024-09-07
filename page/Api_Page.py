import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


api_url = "https://web-gate.chitai-gorod.ru/api"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjU4MjcwNTEsImlhdCI6MTcyNTY1OTA1MSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImY2YTY0MjY0M2RhMTIwNGJmMmIyMjk3ZDBjMGRjMzUxNGI1ZGRlYTUzYzFjNjg5ZDA2OGZmOTRiZThlN2RjMjUiLCJ0eXBlIjoxMH0._i9m9n617we_OztYtqgOjofP35obTt7pnDyETiJsN_U"


class ApiPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = api_url
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url
