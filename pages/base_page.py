from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    @allure.step("Выполнить JavaScript скрипт")
    def execute_script(self, script, element=None):
        if element:
            return self.driver.execute_script(script, element)
        return self.driver.execute_script(script)

    @allure.step("Переключиться на окно с индексом {index}")
    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидать URL {url}")
    def wait_for_url(self, url):
        return self.wait.until(EC.url_to_be(url))

    @allure.step("Ожидать, что URL содержит {pattern}")
    def wait_for_url_contains(self, pattern):
        return self.wait.until(EC.url_contains(pattern))
    
    @allure.step("Ожидать открытия нового окна")
    def wait_for_new_window(self, original_window, timeout=10):
        self.wait.until(lambda driver: len(driver.window_handles) > len([original_window]))