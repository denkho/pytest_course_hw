import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    drvr = webdriver.Chrome()
    yield drvr
    print("\nquit browser")
    drvr.quit()
    