import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from constants import ui_url


class Ui_CartPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = ui_url
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("Политика куки")
    def set_cookie_policy(self):
        cookie = {"name": "cookie_policy", "value": "1"}
        self.__driver.add_cookie(cookie)

    @allure.step("Проверка пустой корзины")
    def get_empty_result_message(self):
        self.__driver.get("https://www.chitai-gorod.ru/cart")
        txt = self.__driver.find_element(
            By.XPATH, '//div[contains(text(),"В корзине")]').text
        return txt
