import allure

from conftest import driver, create_user, login_in_system
from page_objects.order_feed_page import OrderFeedPage as OFP
from page_objects.main_page import MainPage as MP
from helper import CreateOrder as CO

class TestOrderFeedPage:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_appearance_order_details_window(self, driver):
        main_page = MP(driver)
        order_feed_page = OFP(driver)
        main_page.wait_overlay_not_displayed()
        main_page.click_orders_feed_button_in_header()
        order_feed_page.click_order()
        assert order_feed_page.wait_orders_info()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_checking_user_orders_in_history_orders(self, driver, create_user, login_in_system):
        main_page = MP(driver)
        order_feed_page = OFP(driver)
        new_order = CO()
        new_order.create_order(create_user)
        order = str(new_order.get_user_orders(create_user))
        main_page.click_orders_feed_button_in_header()
        main_page.wait_order_feed_form()
        numbers_orders = order_feed_page.get_numbers_orders()
        assert order in numbers_orders


    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_completed_all_time_is_incremented(self, driver, create_user, login_in_system):
        main_page = MP(driver)
        order_feed_page = OFP(driver)
        new_order = CO()
        main_page.click_orders_feed_button_in_header()
        order_counter_1 = order_feed_page.get_counter_all_orders()
        new_order.create_order(create_user)
        order_counter_2 = order_feed_page.get_counter_all_orders()
        assert order_counter_2 > order_counter_1

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_completed_daily_is_incremented(self, driver, create_user, login_in_system):
        main_page = MP(driver)
        order_feed_page = OFP(driver)
        new_order = CO()
        main_page.click_orders_feed_button_in_header()
        order_counter_1 = order_feed_page.get_counter_daily_orders()
        new_order.create_order(create_user)
        order_counter_2 = order_feed_page.get_counter_daily_orders()
        assert order_counter_2 > order_counter_1

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_user_order_in_section_in_progress(self, driver, create_user, login_in_system):
        main_page = MP(driver)
        order_feed_page = OFP(driver)
        new_order = CO()
        main_page.click_orders_feed_button_in_header()
        new_order.create_order(create_user)
        order_in_progress = order_feed_page.get_orders_in_progress()
        order = str(new_order.get_user_orders(create_user))
        assert order in order_in_progress