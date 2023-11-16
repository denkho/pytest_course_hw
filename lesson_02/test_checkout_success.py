from selenium.webdriver.common.by import By
import data, locators


def item_name_to_selector_button(name: str, button: str) -> str:
    """Функция для преобразования названия продукта в 
    корректный селектор"""
    return f"{button.lower()}-{'-'.join(name.lower().split())}"


def test_checkout_positive(driver, authorise):
    item_name = driver.find_element(*locators.INVENTORY_ITEM_WITH_SPACE).text
    item_name_selector = item_name_to_selector_button(item_name, 'add-to-cart')

    driver.find_element(By.XPATH, '//button[@data-test="' + item_name_selector + '"]').click()
    
    driver.implicitly_wait(3)
    driver.get(data.CART_URL)
    assert driver.current_url == data.CART_URL, "Переход в корзину не удался"

    assert driver.find_element(*locators.INVENTORY_ITEM).text == item_name, "В корзине отсутствует выбранный товар"
    driver.implicitly_wait(3)

    driver.find_element(*locators.CHECKOUT_BUTTON).click()
    driver.implicitly_wait(3)

    assert driver.current_url == data.CHECHOUT_STEPONE_URL, "Не перешли на первый шаг, где требуется введение данных пользователя"
    driver.find_element(*locators.CHECKOUT_FIRST_NAME).send_keys(data.NAME_ADDRESS["first_name"])
    driver.find_element(*locators.CHECKOUT_LAST_NAME).send_keys(data.NAME_ADDRESS["last_name"])
    driver.find_element(*locators.CHEKCOUT_POSTAL_CODE).send_keys(data.NAME_ADDRESS["zip"])

    driver.find_element(*locators.CONTINUE_BUTTON).click()
    driver.implicitly_wait(3)

    assert driver.current_url == data.CHECHOUT_STEPTWO_URL, "Не перешли на второй шаг"
    assert driver.find_element(*locators.INVENTORY_ITEM).text == item_name, "В корзине отсутствует выбранный товар на втором шаге чекаута"

    driver.find_element(*locators.FINISH_BUTTON).click()
    driver.implicitly_wait(3)

    assert driver.current_url == data.CHECHOUT_COMPLETE, "Что-то случилось на последнем шаге после нажатия кнопки финиш"
    assert driver.find_element(*locators.CHECKOUT_TITLE).text == data.CHECKOUT_COMPLETE_TEXT, "Отсутствует title с текстом, либо изменился текст"
    assert driver.find_element(*locators.CHECKOUT_COMPLETE_HEADER).text == data.THANKS_FOR_ORDER_TEXT, "Отсутствует текст с благодарностью, либо изменился"
    