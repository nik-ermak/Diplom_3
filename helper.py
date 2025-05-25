import allure
import requests
from faker import Faker

from data import Ingredients
from urls_for_tests import Endpoints as END

class DataForCreateUser:
    # Метод генерации пользователя
    @staticmethod
    def generate_fake_data_for_create_user():
        fake = Faker()
        email = f'{fake.email()}{fake.random_number(digits=3)}'
        password = fake.password(length=6)
        name = fake.first_name()
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        return payload


class CreateOrder:
    @allure.step('Создание заказа')
    def create_order(self, create_user):
        token = create_user[1].json()['accessToken']
        requests.post(END.CREATE_ORDER, headers={'Authorization': token}, data=Ingredients.INGREDIENTS)
        # return response.json()['order']['number']

    @allure.step('Получение заказа пользователя')
    def  get_user_orders(self, create_user):
        token = create_user[1].json()['accessToken']
        response = requests.get(END.GET_ORDERS, headers= {'Authorization': token})
        return response.json()['orders'][0]['number']