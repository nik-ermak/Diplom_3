import allure

from conftest import driver
from page_objects.recovery_password_page import RecoveryPasswordPage as RPP
from helper import DataForCreateUser as DFCU
from page_objects.main_page import MainPage as MP
from page_objects.auth_page import AuthPage as AP

class TestRecoveryPasswordPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_transfer_to_recovery_password_page(self, driver):
        recovery_password_page = RPP(driver)
        auth_page = AP(driver)
        main_page = MP(driver)
        main_page.click_personal_account_button_in_header()
        auth_page.click_on_recovery_button()
        assert recovery_password_page.wait_recovery_password_form()

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_and_click_on_recovery_button(self, driver):
        recovery_password_page = RPP(driver)
        auth_page = AP(driver)
        main_page = MP(driver)
        main_page.click_personal_account_button_in_header()
        auth_page.click_on_recovery_button()
        recovery_password_page.send_email_field(DFCU.generate_fake_data_for_create_user()['email'])
        recovery_password_page.click_on_recover_password_button()
        assert recovery_password_page.wait_save_password_button()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_active_password_field(self, driver):
        recovery_password_page = RPP(driver)
        auth_page = AP(driver)
        main_page = MP(driver)
        main_page.click_personal_account_button_in_header()
        auth_page.click_on_recovery_button()
        recovery_password_page.send_email_field(DFCU.generate_fake_data_for_create_user()['email'])
        recovery_password_page.click_on_recover_password_button()
        recovery_password_page.send_password_field(DFCU.generate_fake_data_for_create_user()['password'])
        recovery_password_page.click_on_show_password_button()
        assert recovery_password_page.password_field_active()