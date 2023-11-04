from selenium import webdriver
import locators, data


def item_name_to_selector_button(name: str, button: str) -> str:
    return f"{button.lower()}-{'-'.join(name.lower().split())}"


def check_exists_by_xpath(xpath):
    """Check if element is present on the page. For empty cart"""
    try:
        webdriver.find_element_by_xpath(xpath)
    except AttributeError:
        return False
    return True


def test_burger_menu_logout(driver, authorise):
    """Checks if is possible to log out through burger menu"""

    driver.find_element(*locators.BURGER_MENU_BUTTON_ICON).click()
    driver.implicitly_wait(3)

    driver.find_element(*locators.BURGER_MENU_LOGOUT_TEXT).click()
    driver.implicitly_wait(3)

    assert driver.current_url == data.MAIN_URL


def test_about_button_burger_menu(driver, authorise):
    """Checks if the About button is active"""

    driver.find_element(*locators.BURGER_MENU_BUTTON_ICON).click()
    driver.implicitly_wait(3)

    driver.find_element(*locators.BURGER_MENU_ABOUT).click()

    assert driver.current_url == data.ABOUT_URL


def test_reset_button_burger_menu(driver, authorise):
    """Checks if the "Reset App State" button works"""
    
    driver.find_element(*locators.ADD_TO_CART_BACKPACK).click()
    driver.find_element(*locators.ADD_TO_CART_BOLTTSHIRT).click()

    driver.implicitly_wait(3)
    driver.get(data.CART_URL)
  
    assert driver.find_element(*locators.INVENTORY_ITEM).text in locators.ITEMS
    assert driver.find_element(*locators.INVENTORY_ITEM).text in locators.ITEMS
    driver.implicitly_wait(3)
    
    driver.get(data.INVENTORY_URL)
    driver.find_element(*locators.BURGER_MENU_BUTTON_ICON).click()
    driver.implicitly_wait(3)

    driver.find_element(*locators.BURGER_MENU_RESET).click()
    driver.implicitly_wait(3)

    driver.get(data.CART_URL)
    driver.implicitly_wait(3)
    assert check_exists_by_xpath(locators.REMOVE_BUTTON) == False
    