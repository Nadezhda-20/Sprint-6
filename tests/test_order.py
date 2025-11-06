import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.test_data import TestData
from data.urls import Urls

class TestOrder:
    @allure.title("Проверка успешного заказа через {order_button} кнопку")
    @pytest.mark.parametrize("order_button,test_data", [
        ("top", TestData.ORDER_DATA_1),
        ("bottom", TestData.ORDER_DATA_2)
    ])
    def test_successful_order(self, driver, order_button, test_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        # Нажимаем на кнопку заказа
        if order_button == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()
        
        # Заполняем первую страницу заказа
        order_page.fill_first_page(
            test_data["first_name"],
            test_data["last_name"], 
            test_data["address"],
            test_data["phone"]
        )
        
        # Заполняем вторую страницу заказа
        order_page.fill_second_page(
            test_data["delivery_date"],
            test_data["rental_period"],
            test_data["color"],
            test_data["comment"]
        )
        
        # Подтверждаем заказ
        order_page.confirm_order()
        
        # Проверяем, что сообщение об успешном заказе отображается
        assert order_page.is_success_message_displayed()

    @allure.title("Проверка редиректа по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        # Переходим на страницу заказа
        main_page.click_order_button_top()
        
        # Кликаем на логотип Самоката
        main_page.click_scooter_logo()
        
        # Проверяем, что вернулись на главную страницу
        main_page.wait_for_url(Urls.MAIN_PAGE)

    @allure.title("Проверка редиректа по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        
        # Сохраняем текущее окно
        main_window = driver.current_window_handle
        
        # Кликаем на логотип Яндекса
        main_page.click_yandex_logo()
        
        # Ждем открытия новой вкладки
        main_page.wait_for_new_window(main_window)
        
        # Переключаемся на новую вкладку
        main_page.switch_to_window(1)
        
        # Проверяем, что открылась страница Дзена
        main_page.wait_for_url_contains("dzen.ru")