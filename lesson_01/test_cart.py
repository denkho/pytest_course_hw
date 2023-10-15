from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

URL = "https://www.saucedemo.com/"
URL_INVENTORY = "https://www.saucedemo.com/inventory.html"
URL_CART = "https://www.saucedemo.com/cart.html"
URL_ITEM = "https://www.saucedemo.com/inventory-item.html?id=4"
URL_ITEM_PARTIAL = "https://www.saucedemo.com/inventory-item.html"
USER_NAME = "standard_user"
PASSWD = "secret_sauce"
ITEMS = ["Sauce Labs Bolt T-Shirt", "Sauce Labs Backpack"]

# Предусловие - залогинится с валидными данными
def login():
    driver.get(URL)
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys(USER_NAME)
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys(PASSWD)
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()


def check_exists_by_xpath(xpath):
    """Check if element is present on the page. For empty cart"""
    try:
        webdriver.find_element_by_xpath(xpath)
    except AttributeError:
        return False
    return True


def item_name_to_selector_button(name: str, button: str) -> str:
    return f"{button.lower()}-{'-'.join(name.lower().split())}"


def test_cart_add_through_inventory():
    """Checks whether it is possible to add products to the cart via product catalog"""
    login()

    driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    # driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    driver.get(URL_CART)
    time.sleep(2)
    assert driver.current_url == URL_CART

    assert driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text in ITEMS
    assert driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text in ITEMS



def test_cart_remove_items():
    """Checks if it is possible to remove products from the cart."""
    driver.find_element(By.XPATH, '//button[starts-with(@data-test, "remove")]').click()
    driver.find_element(By.XPATH, '//button[starts-with(@data-test, "remove")]').click()
    
    assert check_exists_by_xpath('//button[starts-with(@data-test, "remove")]') == False


def test_cart_add_through_item_card():
    """Check if is possible to add item from item card to the cart"""

    driver.get(URL_ITEM)
    time.sleep(2)
    # Save item name to check it in the cart
    item_name = driver.find_element(By.XPATH, '//div[@class="inventory_details_name large_size"]').text
    item_name_selector = item_name_to_selector_button(item_name, 'add-to-cart')

    driver.find_element(By.XPATH, '//button[@data-test="' + item_name_selector + '"]').click()

    driver.get(URL_CART)
    time.sleep(2)
    assert driver.find_element(By.LINK_TEXT, item_name)


def test_cart_remove_through_item_card():
    """Check if is possible to remove the item via item card"""

    driver.get(URL_ITEM)
    time.sleep(2)
    item_name = driver.find_element(By.XPATH, '//div[@class="inventory_details_name large_size"]').text
    item_name_selector_remove = item_name_to_selector_button(item_name, 'Remove') 
    driver.find_element(By.XPATH, '//button[@data-test="' + item_name_selector_remove + '"]').click()

    driver.get(URL_CART)
    time.sleep(2)    
    assert check_exists_by_xpath('//button[starts-with(@data-test, "remove")]') == False

    driver.quit()

    

