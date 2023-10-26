from selenium.webdriver.common.by import By
import data
import locators

def test_login_form(driver):
    """Проверяем позитивный сценарий логина с корректными данными"""
    driver.get(data.MAIN_URL)

    driver.find_element(By.XPATH, locators.LOGIN_FIELD).send_keys(data.LOGIN)
    driver.find_element(By.XPATH, locators.PASSWORD_FIELD).send_keys(data.PASSWORD)
    driver.find_element(By.XPATH, locators.LOGIN_BUTTON).click()

    driver.implicitly_wait(5)

    assert driver.current_url == data.INVENTORY_URL, "Positive login failed"


# Разлогиниваемся для следующего теста

def test_login_form_negative(driver):
    driver.get(data.MAIN_URL)

    driver.find_element(By.XPATH, locators.LOGIN_FIELD).send_keys(data.LOGIN_NEGATIVE)
    driver.find_element(By.XPATH, locators.PASSWORD_FIELD).send_keys(data.PASSWORD_NEGATIVE)
    driver.find_element(By.XPATH, locators.LOGIN_BUTTON).click()

    driver.implicitly_wait(5)
    
    error_message = driver.find_element(By.XPATH, locators.ERROR_MESSAGE_LOGIN_FORM).text
    assert  error_message == "Epic sadface: Username and password do not match any user in this service", "Negative login failed"

    