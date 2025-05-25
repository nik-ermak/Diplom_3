import allure

from locators.order_feed_page_locators import LocatorsOrderFeed as LOF
from page_objects.base_page import BasePage

class OrderFeedPage(BasePage):
    @allure.step('Ожидание формы заказа')
    def wait_orders_info(self):
        return self.wait_for_element(LOF.window_order_info)

    @allure.step('Получение количества заказов Выполнено за всё время')
    def get_counter_all_orders(self):
        return self.get_text_of_element(LOF.list_total_orders)

    @allure.title('Получение количества заказов Выполнено за сегодня')
    def get_counter_daily_orders(self):
        return self.get_text_of_element(LOF.list_daily_orders)

    @allure.step('Получение номеров заказов')
    def get_numbers_orders(self):
        orders = self.get_text_of_multiple_element(LOF.history_orders)
        numbers_order_list = []
        for order in orders:
            order_number = order.text[2:]
            numbers_order_list.append(order_number)
        return numbers_order_list

    @allure.step('Получение заказов В работе')
    def get_orders_in_progress(self):
        orders_in_job_progress = []
        orders = self.get_text_of_multiple_element(LOF.orders_in_progress)
        for i in orders:
            order_number = i.text[1:]
            orders_in_job_progress.append(order_number)
        return orders_in_job_progress

    @allure.step('Клик по заказу')
    def click_order(self):
        self.click_on_element(LOF.order_in_history)