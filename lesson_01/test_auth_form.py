from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

URL = "https://www.saucedemo.com/"

def test_login_form_positive():
    """Позитивные тесты для проверки авторизации"""
    driver.get(URL)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    passwd_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    passwd_field.send_keys("secret_sauce")

    lgn_btn = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    lgn_btn.click()

    time.sleep(5)
    
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    burger_menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
    burger_menu.click()

    time.sleep(5)

    logout_link =  driver.find_element(By.LINK_TEXT, 'Logout')
    logout_link.click()

    time.sleep(5)

    assert driver.current_url == URL

    driver.quit()


