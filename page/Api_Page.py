import allure
import requests
from selenium.webdriver.remote.webdriver import WebDriver
from constants import base_url, search, headers


class Api_Page:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = base_url
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Поиск книги на кириллице")
    def ru_get(self) -> None:
        resp = requests.get(base_url+search+"гарри", headers=headers)
        return resp

    @allure.step("Поиск книги на латинице")
    def eng_get(self) -> None:
        resp = requests.get(base_url+search+'harry', headers=headers)
        return resp

    @allure.step("Поиск книги по автору")
    def author_get(self) -> None:
        resp = requests.get(base_url+search+'Михаил Булгаков', headers=headers)
        return resp

    @allure.step("Поиск книги по серии")
    def series_get(self) -> None:
        resp = requests.get(base_url+search+'гарри поттер', headers=headers)
        return resp

    @allure.step("Поиск книги по жанру")
    def fiction_get(self) -> None:
        resp = requests.get(base_url+search+'Классическая литература', headers=headers)
        return resp

    @allure.step("Поиск канцелярии")
    def prod_get(self) -> None:
        resp = requests.get(base_url+search+'Канцелярия', headers=headers)
        return resp

    @allure.step("Поиск неправильным методом")
    def prod_delete(self) -> None:
        resp = requests.delete(base_url+search+'Канцелярия', headers=headers)
        return resp

    @allure.step("Поиск спецсимволы")
    def neg_get(self) -> None:
        resp = requests.get(base_url+search+'.№#$%&!?', headers=headers)
        return resp

    @allure.step("Поиск пустой")
    def empty_get(self) -> None:
        resp = requests.get(base_url+search+'', headers=headers)
        return resp
