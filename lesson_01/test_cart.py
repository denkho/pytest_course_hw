from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

URL = "https://www.saucedemo.com/"
URL_CART = "https://www.saucedemo.com/cart.html"
USER_NAME = "standard_user"
PASSWD = "secret_sauce"
ITEMS = ["Sauce Labs Bolt T-Shirt", "Sauce Labs Backpack"]

# Предусловие - залогинится с валидными данными
def login():
    driver.get(URL)
    time.sleep(5)
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys(USER_NAME)
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys(PASSWD)
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

# Добавляем товары в корзину
def test_cart_add():
    login()
    time.sleep(5)

    driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()

    time.sleep(5)

    assert driver.current_url == URL_CART

    assert driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text in ITEMS
    assert driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text in ITEMS

    time.sleep(5)

    driver.quit()
# //*[@class="inventory_item"]//div[@class="inventory_item_name"].text()
# //*[@class="inventory_item"]//button[@data-test="add-to-cart-sauce-labs-backpack"]
    

