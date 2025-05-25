import allure

from page_objects.personal_account_page import PersonalAccountPage as PAP
from page_objects.main_page import MainPage as MP
from page_objects.auth_page import AuthPage as AP
from conftest import driver, create_user, login_in_system

class TestPersonalAccountPage:
    @allure.title('Переход в Личный кабинет пользователя')
    def test_transfer_to_personal_account(self, driver, create_user, login_in_system):
        main_page = MP(driver)
        personal_account_page = PAP(driver)
        main_page.click_personal_account_button_in_header()
        assert personal_account_page.wait_profile_form()

    @allure.title('Переход в раздел История заказов в Личном кабинете')
    def test_transfer_to_user_history_orders(self, driver, create_user, login_in_system):
        main_page = MP(driver)
        personal_account_page = PAP(driver)
        main_page.click_personal_account_button_in_header()
        personal_account_page.click_history_orders()
        assert personal_account_page.wait_profile_form()

    @allure.title('Выход из аккаунта')
    def test_logout_of_account(self, driver, create_user, login_in_system):
        main_page = MP(driver)
        personal_account_page = PAP(driver)
        auth_page = AP(driver)
        main_page.click_personal_account_button_in_header()
        personal_account_page.click_logout_button()
        assert auth_page.wait_authorization_form()