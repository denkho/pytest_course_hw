import data
import locators


def login(driver):
    """Функция для авторизации в тестах"""
    driver.get(data.MAIN_URL)
    driver.implicitly_wait(3)
    driver.find_element(*locators.LOGIN_FIELD).send_keys(data.LOGIN)
    driver.find_element(*locators.PASSWORD_FIELD).send_keys(data.PASSWORD)
    driver.find_element(*locators.LOGIN_BUTTON).click()


def test_inventory_AZ_filter(driver):
    """Тест фильтра AZ"""
    login(driver)

    # собираем перечень названий элементов в список для последующей проверки фильтром
    items = driver.find_elements(*locators.INVENTORY_ITEM)
    items_lst_start = [item.text for item in items]
    
    driver.find_element(*locators.SORT_CONTAINER).click()
    driver.find_element(*locators.ZA_FILTER).click()
    driver.find_element(*locators.AZ_FILTER).click()
    
    # после фильтрования собираем перечень названий элементов в список
    items = driver.find_elements(*locators.INVENTORY_ITEM)
    items_lst_filtered = [item.text for item in items]

    assert sorted(items_lst_start) == items_lst_filtered


def test_inventory_ZA_filter(driver):
    """Тест фильтра ZA"""
    login(driver)
    # собираем перечень названий элементов в список для последующей проверки фильтром
    items = driver.find_elements(*locators.INVENTORY_ITEM)
    items_lst_start = [item.text for item in items]
    
    driver.find_element(*locators.SORT_CONTAINER).click()
    driver.find_element(*locators.ZA_FILTER).click()
    
    # после фильтрования собираем перечень названий элементов в список
    items = driver.find_elements(*locators.INVENTORY_ITEM)
    items_lst_filtered = [item.text for item in items]

    assert sorted(items_lst_start, reverse=True) == items_lst_filtered

