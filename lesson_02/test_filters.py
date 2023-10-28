import locators

def test_inventory_AZ_filter(driver, authorise):
    """Тест фильтра AZ"""

    # собираем перечень названий элементов в список для последующей проверки фильтром
    items = driver.find_elements(*locators.INVENTORY_ITEM)
    items_lst_start = [item.text for item in items]
    
    driver.find_element(*locators.SORT_CONTAINER).click()
    driver.find_element(*locators.ZA_FILTER).click()
    driver.find_element(*locators.AZ_FILTER).click()
    driver.implicitly_wait(3)

    # после фильтрования собираем перечень названий элементов в список
    items = driver.find_elements(*locators.INVENTORY_ITEM)
    items_lst_filtered = [item.text for item in items]

    assert sorted(items_lst_start) == items_lst_filtered


def test_inventory_ZA_filter(driver, authorise):
    """Тест фильтра ZA"""

    # собираем перечень названий элементов в список для последующей проверки фильтром
    items = driver.find_elements(*locators.INVENTORY_ITEM)
    items_lst_start = [item.text for item in items]
    
    driver.find_element(*locators.SORT_CONTAINER).click()
    driver.find_element(*locators.ZA_FILTER).click()
    driver.implicitly_wait(3)

    # после фильтрования собираем перечень названий элементов в список
    items = driver.find_elements(*locators.INVENTORY_ITEM)
    items_lst_filtered = [item.text for item in items]

    assert sorted(items_lst_start, reverse=True) == items_lst_filtered

def test_inventory_price_low_high_sort_filter(driver, authorise):
    """Тест фильтра цен от низкой к высокой"""

    # собираем список цен элементов
    prices = driver.find_elements(*locators.INVENTORY_ITEM_PRICE)
    prices_lst_start = [float(p.text[1:]) for p in prices]

    # включаем фильтр по ценам с меньшей к большей
    driver.find_element(*locators.SORT_CONTAINER).click()
    driver.find_element(*locators.LOHI_FILTER).click()
    driver.implicitly_wait(3)

    # собираем список цен элементов после фильтрования
    prices = driver.find_elements(*locators.INVENTORY_ITEM_PRICE)
    prices_lst_filtered = [float(p.text[1:]) for p in prices]

    # сравниваем, что получилось
    assert sorted(prices_lst_start) == prices_lst_filtered


def test_inventory_price_high_low_sort_filter(driver, authorise):
    """Тест фильтра цен от высокой к низкой"""

    # собираем список цен элементов
    prices = driver.find_elements(*locators.INVENTORY_ITEM_PRICE)
    prices_lst_start = [float(p.text[1:]) for p in prices]

    # включаем фильтр по ценам от большей к меньшей
    driver.find_element(*locators.SORT_CONTAINER).click()
    driver.find_element(*locators.HILO_FILTER).click()
    driver.implicitly_wait(3)

    # собираем список цен элементов после фильтрования
    prices = driver.find_elements(*locators.INVENTORY_ITEM_PRICE)
    prices_lst_filtered = [float(p.text[1:]) for p in prices]

    # сравниваем, что получилось
    assert sorted(prices_lst_start, reverse=True) == prices_lst_filtered
