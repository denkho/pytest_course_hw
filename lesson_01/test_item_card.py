from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

URL = "https://www.saucedemo.com/"
URL_ITEM = "https://www.saucedemo.com/inventory-item.html?id=4"
URL_INVENTORY = "https://www.saucedemo.com/inventory.html"
USER_NAME = "standard_user"
PASSWD = "secret_sauce"

# Предусловие - залогинится с валидными данными
def login():
    driver.get(URL)
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys(USER_NAME)
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys(PASSWD)
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

def test_go_to_item_from_inventory_by_item_title():
    login()

    item_name = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text
    driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').click()
    time.sleep(3)
    assert URL_ITEM in driver.current_url
    assert driver.find_element(By.XPATH, '//div[@class="inventory_details_name large_size"]').text == item_name 


def test_go_to_item_from_inventory_by_item_image():

    driver.get(URL_INVENTORY)
    time.sleep(3)
    item_name = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text
    driver.find_element(By.XPATH, '//img[@class="inventory_item_img"]').click()
    print(item_name)
    assert URL_ITEM in driver.current_url
    assert driver.find_element(By.XPATH, '//div[@class="inventory_details_name large_size"]').text == item_name 
    driver.quit()
