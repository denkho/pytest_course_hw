from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(options=options)


URL = "https://www.saucedemo.com/"
URL_CART = "https://www.saucedemo.com/cart.html"
URL_INVENTORY = "https://www.saucedemo.com/inventory.html"
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


def item_name_to_selector_button(name: str, button: str) -> str:
    return f"{button.lower()}-{'-'.join(name.lower().split())}"


def check_exists_by_xpath(xpath):
    """Check if element is present on the page. For empty cart"""
    try:
        webdriver.find_element_by_xpath(xpath)
    except AttributeError:
        return False
    return True


def test_burger_menu_logout():
    """Checks if is possible to log out through burger menu"""
    login()

    assert driver.current_url == URL_INVENTORY
    driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, 'Logout').click()

    time.sleep(5)

    assert driver.current_url == URL


def test_about_button_burger_menu():
    """Checks if the About button is active"""
    login()

    assert driver.current_url == URL_INVENTORY

    driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]').click()

    assert driver.current_url == "https://saucelabs.com/"
    driver.get(URL)


def test_reset_button_burger_menu():
    """Checks if the "Reset App State" button works"""
    login()
    
    driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    time.sleep(3)
    driver.get(URL_CART)

    assert driver.current_url == URL_CART    
    assert driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text in ITEMS
    assert driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text in ITEMS
    time.sleep(3)
    
    driver.get(URL_INVENTORY)
    driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//a[@id="reset_sidebar_link"]').click()
    time.sleep(5)

    driver.get(URL_CART)
    time.sleep(2)    
    assert check_exists_by_xpath('//button[starts-with(@data-test, "remove")]') == False

    driver.quit()
