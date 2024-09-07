import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()
