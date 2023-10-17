from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()

URL = "https://www.saucedemo.com/"
URL_CART = "https://www.saucedemo.com/cart.html"
URL_CHECKOUT_STEPONE = "https://www.saucedemo.com/checkout-step-one.html"
URL_CHECKOUT_STEPTWO = "https://www.saucedemo.com/checkout-step-two.html"
URL_CHECKOUT_COMPELETE = "https://www.saucedemo.com/checkout-complete.html"
USER_NAME = "standard_user"
PASSWD = "secret_sauce"
NAME_ADDRESS = {"first_name": "Peter", "last_name": "Smith", "zip": "33333"}

# Предусловие - залогинится с валидными данными
def login():
    driver.get(URL)
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys(USER_NAME)
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys(PASSWD)
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()


def item_name_to_selector_button(name: str, button: str) -> str:
    return f"{button.lower()}-{'-'.join(name.lower().split())}"

def test_checkout_positive():
    login()
    
    time.sleep(10)
    item_name = driver.find_element(By.XPATH, '//div[@class="inventory_item_name "]').text
    item_name_selector = item_name_to_selector_button(item_name, 'add-to-cart')

    driver.find_element(By.XPATH, '//button[@data-test="' + item_name_selector + '"]').click()
    
    time.sleep(3)
    driver.get(URL_CART)

    assert driver.current_url == URL_CART    
    assert driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text == item_name
    time.sleep(3)

    driver.find_element(By.XPATH, '//button[@data-test="checkout"]').click()
    time.sleep(3)

    assert driver.current_url == URL_CHECKOUT_STEPONE

    driver.find_element(By.XPATH, '//input[@data-test="firstName"]').send_keys(NAME_ADDRESS["first_name"])
    driver.find_element(By.XPATH, '//input[@data-test="lastName"]').send_keys(NAME_ADDRESS["last_name"])
    driver.find_element(By.XPATH, '//input[@data-test="postalCode"]').send_keys(NAME_ADDRESS["zip"])

    driver.find_element(By.XPATH, '//input[@data-test="continue"]').click()
    time.sleep(3)

    assert driver.current_url == URL_CHECKOUT_STEPTWO
    assert driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text == item_name

    driver.find_element(By.XPATH, '//button[@data-test="finish"]').click()
    time.sleep(3)

    assert driver.current_url == URL_CHECKOUT_COMPELETE
    assert driver.find_element(By.XPATH, '//span[@class="title"]').text == "Checkout: Complete!"
    assert driver.find_element(By.XPATH, '//h2[@class="complete-header"]').text == "Thank you for your order!"
    

    driver.quit()