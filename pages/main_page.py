from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Кликнуть на вопрос с индексом {question_index}")
    def click_question(self, question_index):
        locator = self.locators.QUESTION_LOCATORS[question_index]
        element = self.scroll_to_element(locator)
        self.click_element(locator)
        # Ожидаем появления ответа вместо time.sleep
        answer_locator = self.locators.ANSWER_LOCATORS[question_index]
        self.wait_for_element_visible(answer_locator)

    @allure.step("Получить текст ответа с индексом {answer_index}")
    def get_answer_text(self, answer_index):
        locator = self.locators.ANSWER_LOCATORS[answer_index]
        element = self.wait_for_element_visible(locator)
        return element.text

    @allure.step("Кликнуть на верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        self.click_element(self.locators.ORDER_BUTTON_TOP)

    @allure.step("Кликнуть на нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        element = self.find_element(self.locators.ORDER_BUTTON_BOTTOM)
        self.scroll_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        self.click_element(self.locators.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(self.locators.SCOOTER_LOGO)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(self.locators.YANDEX_LOGO)