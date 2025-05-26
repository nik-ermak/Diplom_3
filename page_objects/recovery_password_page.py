import allure

from locators.recovery_password_page_locators import LocatorsRecoveryPassword as LRP
from page_objects.base_page import BasePage

class RecoveryPasswordPage(BasePage):
    @allure.step('Ожидание формы восстановления пароля')
    def wait_recovery_password_form(self):
        return self.wait_for_element(LRP.recover_password_form)

    @allure.step('Заполнение поля email')
    def send_email_field(self, email):
        self.send_keys_to_input(LRP.email_field, email)

    @allure.step('Заполнение поля password')
    def send_password_field(self, password):
        self.send_keys_to_input(LRP.new_password_field, password)

    @allure.step('Клик по кнопке Войти')
    def click_on_login_button(self):
        self.click_on_element(LRP.login_button)

    @allure.step('Клик по кнопке Восстановить')
    def click_on_recover_password_button(self):
        self.click_on_element(LRP.recover_password_button)

    @allure.step('Ожидание кнопки Сохранить')
    def wait_save_password_button(self):
        return self.wait_for_element(LRP.save_password_button)

    @allure.step('Клик по кнопке Сохранить')
    def click_on_save_password_button(self):
        self.click_on_element(LRP.save_password_button)

    @allure.step('Заполнение поля Код из письма')
    def send_code_from_email_field(self, code):
        self.send_keys_to_input(LRP.code_from_email_field, code)

    @allure.step('Клик по кнопке скрыть/показать пароль')
    def click_on_show_password_button(self):
        self.move_to_element_and_click(LRP.show_password_button)

    @allure.step('Поле password подсвечивается')
    def password_field_active(self):
        return self.wait_for_element(LRP.password_active_field)