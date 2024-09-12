import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from constants import ui_url


class Ui_MainPage:

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

    @allure.step("Поиск книги на кириллице")
    def rus_search(self, term):
        self.__driver.find_element(
            By.CLASS_NAME, "header-search__input").send_keys(term)
        self.__driver.find_element(
            By.CLASS_NAME, "header-search__button").click()
        txt = self.__driver.find_element(
            By.XPATH, '//p[contains(text(),"Показываем")]').text
        return txt

    @allure.step("Поиск книги на латинице")
    def eng_search(self, term):
        self.__driver.find_element(
            By.CLASS_NAME, "header-search__input").send_keys(term)
        self.__driver.find_element(
            By.CLASS_NAME, "header-search__button").click()
        txt = self.__driver.find_element(
            By.XPATH, '//p[contains(text(),"Показываем")]').text
        return txt

    @allure.step("Пустой поиск")
    def empty_search(self, term):
        self.__driver.find_element(
            By.CLASS_NAME, "header-search__input").send_keys(term)
        self.__driver.find_element(
            By.CLASS_NAME, "header-search__button").click()

    @allure.step("Поиск сразу нескольких книг")
    def books_search(self, term):
        self.__driver.find_element(
            By.CLASS_NAME, "header-search__input").send_keys(term)
        self.__driver.find_element(
            By.CLASS_NAME, "header-search__button").click()
        txt = self.__driver.find_element(
            By.XPATH, '//p[contains(text(),"Показываем")]').text
        return txt

    @allure.step("Поиск по категории")
    def series_search(self, term):
        self.__driver.find_element(
            By.CLASS_NAME, "header-search__input").send_keys(term)
        self.__driver.find_element(
            By.CLASS_NAME, "header-search__button").click()
        txt = self.__driver.find_element(
            By.XPATH, '//p[contains(text(),"Показываем")]').text
        return txt

    @allure.step("Поиск через каталог")
    def catalog_search(self):
        self.__driver.find_element(
            By.XPATH, '//div[contains(text(),"Да, я здесь")]').click()
        self.__driver.find_element(
            By.XPATH, '//span[contains(text(),"Каталог")]').click()
        self.__driver.find_element(
            By.XPATH, '//span[contains(text(),"Художественная литература")]').click()
        self.__driver.find_element(
            By.XPATH, '//span[contains(text(),"Поэзия")]').click()
        txt = self.__driver.find_element(
            By.XPATH, '//h1[contains(text(),"Поэзия")]').text
        return txt

    @allure.step("Проверка фильтра 'Сначала новые'")
    def filter_online(self, term):
        self.__driver.find_element(
            By.CLASS_NAME, "header-search__input").send_keys(term)
        self.__driver.find_element(
            By.CLASS_NAME, "header-search__button").click()
        txt = self.__driver.find_element(
            By.XPATH, '//p[contains(text(),"Показываем")]').text
        self.__driver.find_element(
            By.XPATH, '//div[contains(text(),"По релевантности")]').click()
        self.__driver.find_element(
            By.XPATH, '//div[contains(text(),"Сначала новые")]').click()
        return txt
