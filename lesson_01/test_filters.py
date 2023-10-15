from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

URL = "https://www.saucedemo.com/"
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

def test_inventory_ZA_filter():
    """Checks if ZA filter works"""
    login()

    # собираем перечень названий элементов в список для последующей проверки фильтром
    items = driver.find_elements(By.XPATH, '//div[@class="inventory_item_name"]')
    items_lst_start = [item.text for item in items]
    
    driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]').click()
    driver.find_element(By.XPATH, '//option[@value="za"]').click()
    
    # после фильтрования собираем перечень названий элементов в список
    items = driver.find_elements(By.XPATH, '//div[@class="inventory_item_name"]')
    items_lst_filtered = [item.text for item in items]

    assert sorted(items_lst_start, reverse=True) == items_lst_filtered


def test_inventory_AZ_filter():
    """Checks if AZ filter works"""
    driver.get(URL_INVENTORY)

    # собираем перечень названий элементов в список для последующей проверки фильтром
    items = driver.find_elements(By.XPATH, '//div[@class="inventory_item_name"]')
    items_lst_start = [item.text for item in items]
    
    driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]').click()
    driver.find_element(By.XPATH, '//option[@value="za"]').click()
    driver.find_element(By.XPATH, '//option[@value="az"]').click()
    
    # после фильтрования собираем перечень названий элементов в список
    items = driver.find_elements(By.XPATH, '//div[@class="inventory_item_name"]')
    items_lst_filtered = [item.text for item in items]

    assert sorted(items_lst_start) == items_lst_filtered


def test_inventory_price_low_high_sort_filter():
    """Checks if price low high sort filter works"""
    
    # собираем список цен элементов
    prices = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    prices_lst_start = [float(p.text[1:]) for p in prices]

    # включаем фильтр по ценам с меньшей к большей
    driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]').click()
    driver.find_element(By.XPATH, '//option[@value="lohi"]').click()
    
    # собираем список цен элементов после фильтрования
    prices = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    prices_lst_filtered = [float(p.text[1:]) for p in prices]

    # сравниваем, что получилось
    assert sorted(prices_lst_start) == prices_lst_filtered


def test_inventory_price_high_low_sort_filter():
    """Checks if price high-low sort filter works"""
    
    # собираем список цен элементов
    prices = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    prices_lst_start = [float(p.text[1:]) for p in prices]

    # включаем фильтр по ценам от большей к меньшей
    driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]').click()
    driver.find_element(By.XPATH, '//option[@value="hilo"]').click()
    
    # собираем список цен элементов после фильтрования
    prices = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    prices_lst_filtered = [float(p.text[1:]) for p in prices]

    # сравниваем, что получилось
    assert sorted(prices_lst_start, reverse=True) == prices_lst_filtered

    driver.quit()

