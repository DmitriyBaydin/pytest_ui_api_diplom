import allure
import pytest
import requests
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page.Api_Page import ApiPage


base_url = "https://web-gate.chitai-gorod.ru/api"
headers = {
        'content-type': 'application/json',
        'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjU4MjcwNTEsImlhdCI6MTcyNTY1OTA1MSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImY2YTY0MjY0M2RhMTIwNGJmMmIyMjk3ZDBjMGRjMzUxNGI1ZGRlYTUzYzFjNjg5ZDA2OGZmOTRiZThlN2RjMjUiLCJ0eXBlIjoxMH0._i9m9n617we_OztYtqgOjofP35obTt7pnDyETiJsN_U"        
    }


@allure.title("Поиск по одному слову на кириллице")
@allure.description("Тест проверяет корректный поиск книги по одному слову на кириллице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_rus_lang():
    with allure.step("api. Поиск по одному слову на кириллице через API"):
        resp = requests.get(base_url + '/v2/search/facet-search?customer&phrase=гарри', headers=headers)
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"


@allure.title("Поиск по одному слову на латинице")
@allure.description("Тест проверяет корректный поиск книги по одному слову на латинице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_eng_lang():
    with allure.step("api. Поиск по одному слову на латинице через API"):
        resp = requests.get(base_url + '/v2/search/facet-search?customer&phrase=harry', headers=headers)
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"


@allure.title("Поиск по автору")
@allure.description("Тест проверяет корректный поиск книги по автору")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_author():
    with allure.step("api. Поиск по автору через API"):
        resp = requests.get(base_url + '/v2/search/facet-search?customer&phrase=Михаил Булгаков', headers=headers)
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"


@allure.title("Поиск по серии")
@allure.description("Тест проверяет корректный поиск книги по серии")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_books_series():
    with allure.step("api. Поиск по серии через API"):
        resp = requests.get(base_url + '/v2/search/facet-search?customer&phrase=гарри поттер', headers=headers)
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"


@allure.title("Поиск по жанру")
@allure.description("Тест проверяет корректный поиск книги по жанру")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_fiction():
    with allure.step("api. Поиск по жанру через API"):
        resp = requests.get(base_url + '/v2/search/facet-search?customer&phrase=Классическая литература', headers=headers)
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"


@allure.title("Поиск канцелярии")
@allure.description("Тест проверяет корректный поиск канцелярии")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_other_products():
    with allure.step("api. Поиск канцелярии через API"):
        resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase=Канцелярия', headers=headers)
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"


@allure.title("Негативная проверка поиска через DELETE")
@allure.description("Отправка запроса поиска канцелярии через DELETE")
@allure.feature("DELETE")
@allure.severity("trivial")
@pytest.mark.negative_test
def test_other_products_by_del():
    with allure.step("api. Отправка запроса через DELETE по API, ошибка 405"):
        resp = requests.delete(base_url+'/v2/search/facet-search?customer&phrase=Канцелярия', headers=headers)
        assert resp.headers["Content-Type"] == "text/plain"
        assert resp.status_code == 405


@allure.title("Негативная проверка ввода в поиск знаков")
@allure.description("Тест проверяет ошибку при вводе только знаков")
@allure.feature("READ")
@allure.severity("minor")
@pytest.mark.negative_test
def test_negative_search():
    with allure.step("api. Отправка запроса со знаками через API"):
        resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase=.№#$%&!?', headers=headers)
        assert resp.headers["Content-Type"] == "application/json"
        assert 'Недопустимая поисковая фраза' in resp.text


@allure.title("Пустой поиск")
@allure.description("Тест на пустой поиск")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.negative_test
def test_empty_search():
    with allure.step("api. Отправка пустого поиска через API"):
        resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase= ', headers=headers)
        assert resp.headers["Content-Type"] == "application/json"
        assert 'Phrase должен содержать минимум 2 символа' in resp.text
