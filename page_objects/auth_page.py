import allure


from locators.auth_page_locators import LocatorsAuthPage as LAP
from page_objects.base_page import BasePage

class AuthPage(BasePage):
    @allure.step('Ожидание отображения формы')
    def wait_authorization_form(self):
        return self.wait_for_element(LAP.auth_form)

    @allure.step('Заполнение поля email')
    def send_email_field(self, email):
        self.send_keys_to_input(LAP.email_field, email)

    @allure.step('Заполнения поля password')
    def send_password_field(self, password):
        self.send_keys_to_input(LAP.password_field, password)

    @allure.step('Клик по кнопке Войти')
    def click_on_login_button(self):
        self.click_on_element(LAP.login_in_account_button)

    @allure.step('Клик по кнопке Зарегистрироваться')
    def click_on_registration_button(self):
        self.click_on_element(LAP.registration_button)

    @allure.step('Клик по кнопке Восстановить пароль')
    def click_on_recovery_button(self):
        self.move_to_element_and_click(LAP.recover_password_button)

    @allure.step('Авторизация')
    def authorization_on_the_website(self, email, password):
        self.send_email_field(email)
        self.send_password_field(password)
        self.click_on_login_button()