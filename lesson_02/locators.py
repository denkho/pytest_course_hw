from selenium.webdriver.common.by import By

# AUTHORIZATION

LOGIN_FIELD = (By.XPATH, '//input[@data-test="username"]')
PASSWORD_FIELD = (By.XPATH, '//input[@data-test="password"]')
LOGIN_BUTTON = (By.XPATH, '//input[@data-test="login-button"]')


# BURGER MENU

BURGER_MENU_BUTTON_ICON = (By.XPATH, '//button[@id="react-burger-menu-btn"]')


# MESSAGES

ERROR_MESSAGE_LOGIN_FORM = (By.XPATH, '//h3[@data-test="error"]')


# INVENTORY

INVENTORY_ITEM = (By.XPATH, '//div[@class="inventory_item_name"]')
INVENTORY_ITEM_PRICE = (By.XPATH, '//div[@class="inventory_item_price"]')


# FILTERS

SORT_CONTAINER = (By.XPATH, '//select[@data-test="product_sort_container"]')
ZA_FILTER = (By.XPATH, '//option[@value="za"]')
AZ_FILTER = (By.XPATH, '//option[@value="az"]')
LOHI_FILTER = (By.XPATH, '//option[@value="lohi"]')
HILO_FILTER = (By.XPATH, '//option[@value="hilo"]')
