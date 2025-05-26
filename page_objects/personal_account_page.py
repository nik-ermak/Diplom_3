import allure

from locators.personal_account_page_locators import LocatorsPersonalAccountPage as LPAP
from page_objects.base_page import BasePage

class PersonalAccountPage(BasePage):
    @allure.step('Ожидание формы профиля')
    def wait_profile_form(self):
        return self.wait_for_element(LPAP.personal_account_form)

    @allure.step('Клик по кнопке Профиль')
    def click_profile_button(self):
        self.click_on_element(LPAP.personal_account_button)

    @allure.step('Клик по кнопке История заказов')
    def click_history_orders(self):
        self.click_on_element(LPAP.history_orders_button)

    @allure.step('Ожидание формы Истории заказов')
    def wait_history_orders_form(self):
        return self.wait_for_element(LPAP.history_orders_form)

    @allure.step('Клик по кнопке Сохранить')
    def click_save_button(self):
        self.click_on_element(LPAP.save_button)

    @allure.step('Клик по кнопке Отмена')
    def click_cansel_button(self):
        self.click_on_element(LPAP.cansel_button)

    @allure.step('Клик по кнопке Выход')
    def click_logout_button(self):
        self.click_on_element(LPAP.logout_button)