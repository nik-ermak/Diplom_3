import allure

from page_objects.base_page import BasePage
from locators.main_page_locators import LocatorsMainPage as LMP

class MainPage(BasePage):
    # Хедер
    @allure.step('Клик по кнопке Конструктор в хедере')
    def click_constructor_button_in_header(self):
        self.move_to_element_and_click(LMP.constructor_button)

    @allure.step('Клик по кнопке Лента заказов в хедере')
    def click_orders_feed_button_in_header(self):
        self.move_to_element_and_click(LMP.order_feed_button)

    @allure.step('Клик по кнопке Личный кабинет в хедере')
    def click_personal_account_button_in_header(self):
        self.move_to_element_and_click(LMP.personal_account_button)

    # Основная часть
    @allure.step('Ожидание формы Конструктора')
    def wait_constructor_form(self):
        return self.wait_for_element(LMP.constructor_form)

    @allure.step('Ожидание формы Ленты заказов')
    def wait_order_feed_form(self):
        return self.wait_for_element(LMP.order_feed_form)

    @allure.step('Клик по ингредиенту Флюорисцентная булка')
    def click_fluorescent_bun_link(self):
        self.wait_overlay_not_displayed()
        self.move_to_element_and_click(LMP.fluorescent_bun_link)

    @allure.step('Ожидание окна Детали ингредиента')
    def wait_ingredient_details_window(self):
        return self.wait_for_element(LMP.ingredient_details_window)

    @allure.step('Клик по кнопке закрытия окна Детали ингредиента')
    def click_close_button_ingredient(self):
        self.click_on_element(LMP.close_ingredient_details_button)

    @allure.step('Окно Детали ингредиента не отображается')
    def ingredient_details_window_not_displayed(self):
        return self.checking_element_not_displayed(LMP.ingredient_details_window)

    @allure.step('Перетаскивание элемента в корзину')
    def add_ingredient_in_basket(self):
        self.wait_overlay_not_displayed()
        self.drag_and_drop(LMP.fluorescent_bun_link, LMP.order_basket)

    @allure.step('Клик по кнопке Оформить заказ')
    def click_on_create_order_button(self):
        self.click_on_element(LMP.create_order_button)

    @allure.step('Создание заказа')
    def create_order(self):
        self.add_ingredient_in_basket()
        self.click_on_create_order_button()

    @allure.step('Получение количества ингредиентов в счётчике')
    def get_number_ingredient_in_counter(self):
        return self.get_text_of_element(LMP.counter_ingredient)

    @allure.step('Ожидание окна созданного заказа')
    def wait_window_created_order(self):
        return self.wait_for_element(LMP.window_created_order)

    @allure.step('Закрытие окна созданного заказа')
    def close_window_created_order(self):
        self.wait_element_clickable(LMP.close_button_created_order)
        self.move_to_element_and_click(LMP.close_button_created_order)

    @allure.step('Получение номера заказа')
    def get_number_of_order(self):
        return self.get_text_of_element(LMP.number_of_order)

    @allure.step('Ожидание загрузки основной страницы')
    def wait_main_page(self):
        return self.wait_for_element(LMP.create_order_button)

    @allure.step('Ожидание кликабельности кнопки Лента заказов')
    def wait_clickable_order_feed_button(self):
        return self.wait_element_clickable(LMP.order_feed_button)

    @allure.step('Ожидание кликабельности ингредиента')
    def wait_clickable_ingredient(self):
        return self.wait_element_clickable(LMP.fluorescent_bun_link)

    @allure.step('Ожидание пока пропадёт оверлей')
    def wait_overlay_not_displayed(self):
        return self.checking_element_not_displayed(LMP.OVERLAY)