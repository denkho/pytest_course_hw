import pytest
from selenium import webdriver
import data, locators

@pytest.fixture()
def driver():
    drvr = webdriver.Chrome()
    yield drvr
    print("\nquit browser")
    drvr.quit()


@pytest.fixture()
def authorise(driver):
    """Функция для авторизации в тестах"""
    driver.get(data.MAIN_URL)
    driver.implicitly_wait(3)
    driver.find_element(*locators.LOGIN_FIELD).send_keys(data.LOGIN)
    driver.find_element(*locators.PASSWORD_FIELD).send_keys(data.PASSWORD)
    driver.find_element(*locators.LOGIN_BUTTON).click()