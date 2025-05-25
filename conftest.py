import pytest
import requests

from selenium import webdriver
from helper import DataForCreateUser as DFCU
from data import Ingredients
from urls_for_tests import UrlsForTests as UFT, Endpoints as End
from page_objects.main_page import MainPage
from page_objects.auth_page import AuthPage

@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(UFT.MAIN_URL)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(UFT.MAIN_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def create_user():
    payload = DFCU.generate_fake_data_for_create_user()
    response = requests.post(End.CREATE_URL, data=payload)
    yield payload, response
    token = response.json()['accessToken']
    requests.delete(End.DELETE_URL, headers={"Authorization": token})

@pytest.fixture()
def login_in_system(driver, create_user):
    user = create_user[0]
    auth_page = AuthPage(driver)
    main_page = MainPage(driver)
    main_page.click_personal_account_button_in_header()
    auth_page.authorization_on_the_website(user['email'], user['password'])
    main_page.wait_main_page()

# @pytest.fixture()
# def create_order(create_user):
#     token = create_user[1].json()['accessToken']
#     response = requests.post(End.CREATE_ORDER, headers= {'Authorization': token}, data= Ingredients.INGREDIENTS)
#     return response.json()['order']['number']