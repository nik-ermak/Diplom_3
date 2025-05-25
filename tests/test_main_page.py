import allure

from conftest import driver, create_user, login_in_system
from page_objects.main_page import MainPage as MP

class TestMainPage:
    @allure.title('Переход по клику на кнопку «Конструктор»')
    def test_click_to_constructor_button(self, driver):
        main_page = MP(driver)
        main_page.click_orders_feed_button_in_header()
        main_page.click_constructor_button_in_header()
        assert main_page.wait_constructor_form()

    @allure.title('Переход по клику на кнопку «Лента заказов»')
    def test_click_to_order_feed_button(self, driver):
        main_page = MP(driver)
        main_page.wait_clickable_ingredient()
        main_page.click_orders_feed_button_in_header()
        assert main_page.wait_order_feed_form()

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_appearance_ingredient_details_window(self, driver):
        main_page = MP(driver)
        main_page.wait_clickable_order_feed_button()
        main_page.click_fluorescent_bun_link()
        assert main_page.wait_ingredient_details_window()

    @allure.title('Окно "Детали ингредиента" закрывается кликом по крестику')
    def test_ingredient_details_window_close(self, driver):
        main_page = MP(driver)
        main_page.wait_clickable_ingredient()
        main_page.click_fluorescent_bun_link()
        main_page.wait_ingredient_details_window()
        main_page.click_close_button_ingredient()
        assert main_page.ingredient_details_window_not_displayed()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_ingredient_counter_increases(self, driver):
        main_page = MP(driver)
        main_page.wait_clickable_ingredient()
        main_page.wait_overlay_not_displayed()
        main_page.add_ingredient_in_basket()
        assert main_page.get_number_ingredient_in_counter() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_authorized_user_can_make_order(self, driver, create_user, login_in_system):
        main_page = MP(driver)
        main_page.click_constructor_button_in_header()
        main_page.create_order()
        assert main_page.wait_window_created_order()