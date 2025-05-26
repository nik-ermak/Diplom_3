from selenium.webdriver.common.by import By


class LocatorsAuthPage:
    # Форма авторизации
    auth_form = By.XPATH, './/div[@class = "Auth_login__3hAey"]'
    # Поле ввода email
    email_field = By.XPATH, './/input[@name = "name"]'
    # Поле ввода пароля
    password_field = By.XPATH, './/input[@name = "Пароль"]'
    # Кнопка Зарегистрироваться
    registration_button = By.XPATH, './/a[text() = "Зарегистрироваться"]'
    # Кнопка Войти
    login_in_account_button = By.XPATH, './/button[text() = "Войти"]'
    # Кнопка Восстановить пароль
    recover_password_button = By.XPATH, './/a[text() = "Восстановить пароль"]'
