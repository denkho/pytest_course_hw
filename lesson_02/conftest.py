import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import data, locators



@pytest.fixture()
def options():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--headless')
    return options

@pytest.fixture()
def driver(options):   
    drvr = webdriver.Chrome(options=options)
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