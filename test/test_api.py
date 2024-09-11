import allure
import pytest
from page.Api_Page import Api_Page
from constants import base_url

api = Api_Page(base_url)


@allure.title("Поиск по одному слову на кириллице")
@allure.description(
    "Тест проверяет корректный поиск книги по одному слову на кириллице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_rus_lang():
    with allure.step("api. Поиск по одному слову на кириллице через API"):
        resp = api.ru_get()
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"


@allure.title("Поиск по одному слову на латинице")
@allure.description(
    "Тест проверяет корректный поиск книги по одному слову на латинице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_eng_lang():
    with allure.step("api. Поиск по одному слову на латинице через API"):
        resp = api.eng_get()
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"


@allure.title("Поиск по автору")
@allure.description("Тест проверяет корректный поиск книги по автору")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_author():
    with allure.step("api. Поиск по автору через API"):
        resp = api.author_get()
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"


@allure.title("Поиск по серии")
@allure.description("Тест проверяет корректный поиск книги по серии")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_books_series():
    with allure.step("api. Поиск по серии через API"):
        resp = api.series_get()
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"


@allure.title("Поиск по жанру")
@allure.description("Тест проверяет корректный поиск книги по жанру")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_fiction():
    with allure.step("api. Поиск по жанру через API"):
        resp = api.fiction_get()
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"


@allure.title("Поиск канцелярии")
@allure.description("Тест проверяет корректный поиск канцелярии")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_other_products():
    with allure.step("api. Поиск канцелярии через API"):
        resp = api.prod_get()
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"


@allure.title("Негативная проверка поиска через DELETE")
@allure.description("Отправка запроса поиска канцелярии через DELETE")
@allure.feature("DELETE")
@allure.severity("trivial")
@pytest.mark.negative_test
def test_other_products_by_del():
    with allure.step("api. Отправка запроса через DELETE по API, ошибка 405"):
        resp = api.prod_delete()
        assert resp.headers["Content-Type"] == "text/plain"
        assert resp.status_code == 405


@allure.title("Негативная проверка ввода в поиск знаков")
@allure.description("Тест проверяет ошибку при вводе только знаков")
@allure.feature("READ")
@allure.severity("minor")
@pytest.mark.negative_test
def test_negative_search():
    with allure.step("api. Отправка запроса со знаками через API"):
        resp = api.neg_get()
        assert resp.headers["Content-Type"] == "application/json"
        assert 'Недопустимая поисковая фраза' in resp.text


@allure.title("Пустой поиск")
@allure.description("Тест на пустой поиск")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.negative_test
def test_empty_search():
    with allure.step("api. Отправка пустого поиска через API"):
        resp = api.empty_get()
        assert resp.headers["Content-Type"] == "application/json"
        assert 'Phrase обязательное поле' in resp.text
