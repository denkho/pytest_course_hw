import data
import locators

def test_login_form(driver):
    """Проверяем позитивный сценарий логина с корректными данными"""
    driver.get(data.MAIN_URL)

    driver.implicitly_wait(3)

    driver.find_element(*locators.LOGIN_FIELD).send_keys(data.LOGIN)
    driver.find_element(*locators.PASSWORD_FIELD).send_keys(data.PASSWORD)
    driver.find_element(*locators.LOGIN_BUTTON).click()

    driver.implicitly_wait(3)
    
    assert driver.current_url == data.INVENTORY_URL, "Positive login failed"


def test_login_form_negative(driver):
    """Проверяем негативный сценарий логина с некорректными данными"""
    driver.get(data.MAIN_URL)
    
    driver.implicitly_wait(3)
    
    driver.find_element(*locators.LOGIN_FIELD).send_keys(data.LOGIN_NEGATIVE)
    driver.find_element(*locators.PASSWORD_FIELD).send_keys(data.PASSWORD_NEGATIVE)
    driver.find_element(*locators.LOGIN_BUTTON).click()

    driver.implicitly_wait(3)
    
    error_message = driver.find_element(*locators.ERROR_MESSAGE_LOGIN_FORM).text
    assert  error_message == "Epic sadface: Username and password do not match any user in this service", "Negative login failed"

    