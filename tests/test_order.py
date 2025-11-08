import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.test_data import TestData
from data.urls import Urls 

class TestOrder:
    @allure.title("Проверка успешного заказа через верхнюю кнопку")
    def test_successful_order_top_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        test_data = TestData.ORDER_DATA_1
        
        main_page.click_order_button_top()
        order_page.fill_first_page(
            test_data["first_name"],
            test_data["last_name"], 
            test_data["address"],
            test_data["phone"]
        )
        order_page.fill_second_page(
            test_data["delivery_date"],
            test_data["rental_period"],
            test_data["color"],
            test_data["comment"]
        )
        order_page.confirm_order()
        assert order_page.is_success_message_displayed()

    @allure.title("Проверка успешного заказа через нижнюю кнопку")
    def test_successful_order_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        test_data = TestData.ORDER_DATA_2
        
        main_page.click_order_button_bottom()
        order_page.fill_first_page(
            test_data["first_name"],
            test_data["last_name"], 
            test_data["address"],
            test_data["phone"]
        )
        order_page.fill_second_page(
            test_data["delivery_date"],
            test_data["rental_period"],
            test_data["color"],
            test_data["comment"]
        )
        order_page.confirm_order()
        assert order_page.is_success_message_displayed()

    @allure.title("Проверка редиректа по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.click_order_button_top()
        main_page.click_scooter_logo()
        main_page.wait_for_url(Urls.MAIN_PAGE)

    @allure.title("Проверка редиректа по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        
        main_window = driver.current_window_handle
        main_page.click_yandex_logo()
        main_page.wait_for_new_window(main_window)
        main_page.switch_to_window(1)
        main_page.wait_for_url_contains("dzen.ru")