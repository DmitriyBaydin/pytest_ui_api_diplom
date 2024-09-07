import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from page.Ui_Page import UiPage


@allure.title("Открытие сайта")
@allure.description("Тест проверяет наличие связи с сайтом")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
@allure.step("Открытие веб-страницы в Chrome")
def test_main_page(browser):
    main_page = UiPage(browser)
    main_page.go()
    main_page.set_cookie_policy()


@allure.title("Поиск на кириллице")
@allure.description("Тест проверяет поиск книги на русском языке")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
@allure.step("Открытие веб-страницы и выполнение поиска")
def test_rus_search(browser):
    main_page = UiPage(browser)
    main_page.go()
    main_page.set_cookie_policy()
    text = main_page.rus_search('мастер и маргарита')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:53] == "Показываем результаты по запросу «мастер и маргарита»"


@allure.title("Поиск на латинице")
@allure.description("Тест проверяет поиск книги на английском языке")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
@allure.step("Открытие веб-страницы и выполнение поиска")
def test_eng_search(browser):
    main_page = UiPage(browser)
    main_page.go()
    main_page.set_cookie_policy()
    text = main_page.eng_search('harry potter')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:47] == "Показываем результаты по запросу «harry potter»"


@allure.title("Пустой поиск")
@allure.description("Тест проверяет вылонение пустого поиска")
@allure.feature("READ")
@allure.severity("trivial")
@pytest.mark.negative_test
@allure.step("Открытие веб-страницы и выполнение поиска")
def test_empty_search(browser):
    main_page = UiPage(browser)
    main_page.go()
    main_page.set_cookie_policy()
    main_page.empty_search("")
    url = browser.current_url
    with allure.step("Отсутствие поиска"):
        assert url == "https://www.chitai-gorod.ru/"


@allure.title("Поиск по двум книгам")
@allure.description("Тест на корректное выполнение поиска по двум книгам")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
@allure.step("Открытие веб-страницы и выполнение поиска")
def test_books_search(browser):
    main_page = UiPage(browser)
    main_page.go()
    main_page.set_cookie_policy()
    text = main_page.books_search('Python, Ревизор')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:49] == "Показываем результаты по запросу «python ревизор»"


@allure.title("Поиск по категории")
@allure.description("Тест на корректное выполнение поиска по категории книг")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
@allure.step("Открытие веб-страницы и выполнение поиска")
def test_series_search(browser):
    main_page = UiPage(browser)
    main_page.go()
    main_page.set_cookie_policy()
    text = main_page.series_search('Книги для детей')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:50] == "Показываем результаты по запросу «книги для детей»"


@allure.title("Просмотр акций")
@allure.description("Тест проверяет открытие страницы с промоакциями")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.positive_test
@allure.step("Открытие веб-страницы и выполнение поиска")
def test_promo(browser):
    main_page = UiPage(browser)
    main_page.go()
    main_page.set_cookie_policy()
    text = main_page.promotions()
    url = browser.current_url
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert url == "https://www.chitai-gorod.ru/promotions"


@allure.title("Поиск по каталогу")
@allure.description("Тест на корректное выполнение поиска по каталогу")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.positive_test
@allure.step("Открытие веб-страницы и выполнение поиска")
def test_catalog_search(browser):
    main_page = UiPage(browser)
    main_page.go()
    main_page.set_cookie_policy()
    text = main_page.catalog_search()
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:14] == 'ПОЭЗИЯ И СТИХИ'


@allure.title("Поиск по фильтру")
@allure.description("Тест на корректное выполнение поиска через фильтр")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.positive_test
@allure.step("Открытие веб-страницы и выполнение поиска")
def test_filter_online(browser):
    main_page = UiPage(browser)
    main_page.go()
    main_page.set_cookie_policy()
    text = main_page.filter_online('Собачье сердце')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:49] == 'Показываем результаты по запросу «собачье сердце»'


@allure.title("Проверка пустой корзины")
@allure.description("Тест на сообщение 'В корзине ничего нет' в пустой корзине")
@allure.feature("")
@allure.severity("blocker")
@pytest.mark.positive_test
@allure.step("Открытие веб-страницы и выполнение поиска")
def test_get_empty_result_message(browser):
    main_page = UiPage(browser)
    main_page.go()
    main_page.set_cookie_policy()
    msg = main_page.get_empty_result_message()
    with allure.step("Проверка пустой корзины и сообщение 'В корзине ничего нет'"):
        assert msg == "В корзине ничего нет"
