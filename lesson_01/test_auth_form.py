from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

URL = "https://www.saucedemo.com/"



def test_login_form_positive():
    """Позитивный тест авторизации с корректными данными"""
    driver.get(URL)
    test_data = ["standard_user", "secret_sauce"]

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys(test_data[0])

    passwd_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    passwd_field.send_keys(test_data[1])

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
    

def test_login_form_negative():
    """Негативный тест авторизации с некорректными данными"""
    
    test_data = ["user", "user"]

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys(test_data[0])

    passwd_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    passwd_field.send_keys(test_data[1])

    lgn_btn = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    lgn_btn.click()

    time.sleep(5)
    
    error_message = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
    assert error_message.text == "Epic sadface: Username and password do not match any user in this service"

    assert driver.current_url == URL

    driver.quit()


