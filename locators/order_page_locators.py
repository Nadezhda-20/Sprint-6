from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Локаторы для первой страницы заказа
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//li[@class='select-search__row']//button")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы для второй страницы заказа
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    RENTAL_PERIOD_OPTIONS = {
        "сутки": (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='сутки']"),
        "двое суток": (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='двое суток']")
    }
    COLOR_CHECKBOXES = {
        "black": (By.ID, "black"),
        "grey": (By.ID, "grey")
    }
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Middle')]")

    # Локаторы для модального окна подтверждения
    MODAL_CONFIRM = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")