from selenium.webdriver.common.by import By

# AUTHORIZATION

LOGIN_FIELD = (By.XPATH, '//input[@data-test="username"]')
PASSWORD_FIELD = (By.XPATH, '//input[@data-test="password"]')
LOGIN_BUTTON = (By.XPATH, '//input[@data-test="login-button"]')


# BURGER MENU

BURGER_MENU_BUTTON_ICON = (By.XPATH, '//button[@id="react-burger-menu-btn"]')
BURGER_MENU_LOGOUT_TEXT = (By.LINK_TEXT, 'Logout')
BURGER_MENU_ABOUT = (By.XPATH, '//a[@id="about_sidebar_link"]')
BURGER_MENU_RESET = (By.XPATH, '//a[@id="reset_sidebar_link"]')


# MESSAGES

ERROR_MESSAGE_LOGIN_FORM = (By.XPATH, '//h3[@data-test="error"]')


# INVENTORY

INVENTORY_ITEM = (By.XPATH, '//div[@class="inventory_item_name"]')
INVENTORY_ITEM_PRICE = (By.XPATH, '//div[@class="inventory_item_price"]')
ADD_TO_CART_BACKPACK = (By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
ADD_TO_CART_BOLTTSHIRT = (By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
BUTTON_INVENTORY_PARTIAL = (By.XPATH, '//button[@data-test=')
ITEMS = ["Sauce Labs Bolt T-Shirt", "Sauce Labs Backpack"]


# FILTERS

SORT_CONTAINER = (By.XPATH, '//select[@data-test="product_sort_container"]')
ZA_FILTER = (By.XPATH, '//option[@value="za"]')
AZ_FILTER = (By.XPATH, '//option[@value="az"]')
LOHI_FILTER = (By.XPATH, '//option[@value="lohi"]')
HILO_FILTER = (By.XPATH, '//option[@value="hilo"]')


# CART
REMOVE_BUTTON = (By.XPATH, '//button[starts-with(@data-test, "remove")]')

# CHECKOUT
CHECKOUT_BUTTON = (By.XPATH, '//button[@data-test="checkout"]')
CONTINUE_BUTTON = (By.XPATH, '//input[@data-test="continue"]')
FINISH_BUTTON = (By.XPATH, '//button[@data-test="finish"]')
CHECKOUT_FIRST_NAME = (By.XPATH, '//input[@data-test="firstName"]')
CHECKOUT_LAST_NAME = (By.XPATH, '//input[@data-test="lastName"]')
CHEKCOUT_POSTAL_CODE = (By.XPATH, '//input[@data-test="postalCode"]')
CHECKOUT_TITLE = (By.XPATH, '//span[@class="title"]')
CHECKOUT_COMPLETE_HEADER = (By.XPATH, '//h2[@class="complete-header"]')