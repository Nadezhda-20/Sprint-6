from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Найти элемент по локатору {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти кликабельный элемент по локатору {locator}")
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть на элемент по локатору {locator}")
    def click_element(self, locator):
        element = self.find_clickable_element(locator)
        element.click()

    @allure.step("Ввести текст '{text}' в элемент по локатору {locator}")
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента по локатору {locator}")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step("Прокрутить к элементу по локатору {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step("Ожидать видимости элемента по локатору {locator}")
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Сделать скриншот: {name}")
    def take_screenshot(self, name):
        """Создание скриншота для отладки"""
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        filename = f"{screenshots_dir}/{name}_{int(time.time())}.png"
        self.driver.save_screenshot(filename)
        print(f"Скриншот сохранен: {filename}")
        return filename