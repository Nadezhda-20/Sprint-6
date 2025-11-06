from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
import allure

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @allure.step("Заполнить первую страницу заказа")
    def fill_first_page(self, first_name, last_name, address, phone):
        self.input_text(self.locators.FIRST_NAME_INPUT, first_name)
        self.input_text(self.locators.LAST_NAME_INPUT, last_name)
        self.input_text(self.locators.ADDRESS_INPUT, address)
        
        # Выбор станции метро
        self.click_element(self.locators.METRO_STATION_INPUT)
        self.click_element(self.locators.METRO_STATION_OPTION)
        
        self.input_text(self.locators.PHONE_INPUT, phone)
        self.click_element(self.locators.NEXT_BUTTON)

    @allure.step("Заполнить вторую страницу заказа")
    def fill_second_page(self, delivery_date, rental_period, color, comment):
        # Заполнение даты
        date_input = self.find_element(self.locators.DELIVERY_DATE_INPUT)
        date_input.send_keys(delivery_date)
        date_input.send_keys(Keys.ENTER)
        
        # Выбор срока аренды
        self.click_element(self.locators.RENTAL_PERIOD_DROPDOWN)
        rental_period_locator = self.locators.RENTAL_PERIOD_OPTIONS[rental_period]
        self.click_element(rental_period_locator)
        
        # Выбор цвета
        color_locator = self.locators.COLOR_CHECKBOXES[color]
        self.click_element(color_locator)
        
        # Комментарий
        if comment:
            self.input_text(self.locators.COMMENT_INPUT, comment)
        
        # Нажатие кнопки Заказать
        self.scroll_to_element(self.locators.ORDER_BUTTON)
        self.click_element(self.locators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.wait_for_element_visible(self.locators.MODAL_CONFIRM)
        self.click_element(self.locators.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверить, что сообщение об успешном заказе отображается")
    def is_success_message_displayed(self):
        element = self.wait_for_element_visible(self.locators.SUCCESS_MESSAGE)
        return element.is_displayed()