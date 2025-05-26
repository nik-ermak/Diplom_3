class UrlsForTests:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'

    REGISTER_URL = f'{MAIN_URL}/register'
    LOGIN_URL = f'{MAIN_URL}/login'
    RECOVERY_URL = f'{MAIN_URL}/recovery'
    FEED_URL = f'{MAIN_URL}/feed'

class Endpoints(UrlsForTests):
    # Ручка регистрации пользователя
    CREATE_URL = f'{UrlsForTests.MAIN_URL}/api/auth/register'
    # Ручка авторизации пользователя
    LOGIN_URL = f'{UrlsForTests.MAIN_URL}/api/auth/login'
    # Ручка удаления пользователя
    DELETE_URL = f'{UrlsForTests.MAIN_URL}/api/auth/user'
    # Ручка создания заказа
    CREATE_ORDER = f'{UrlsForTests.MAIN_URL}/api/orders'
    # Ручка получения заказов
    GET_ORDERS = f'{UrlsForTests.MAIN_URL}/api/orders'