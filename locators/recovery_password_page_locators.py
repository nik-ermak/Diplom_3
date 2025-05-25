from selenium.webdriver.common.by import By


class LocatorsRecoveryPassword:
    # Поле для ввода email
    email_field = By.XPATH, './/input[@name = "name"]'
    # Кнопка Восстановить
    recover_password_button = By.XPATH, './/button[text() = "Восстановить"]'
    # Форма восстановления пароля
    recover_password_form = By.XPATH, ".//h2[text() = 'Восстановление пароля']"
    # Поле для ввода нового пароля
    new_password_field = By.XPATH, ".//input[@name = 'Введите новый пароль']"
    # Поля для ввода кода из письма
    code_from_email_field = By.XPATH, ".//label[text() = 'Введите код из письма']"
    # Кнопка Показать пароль
    show_password_button = By.XPATH, ".//div[@class = 'input__icon input__icon-action']"
    # Подсветка поля Пароль
    password_active_field = By.CSS_SELECTOR, ".input.input_status_active"
    # Кнопка Сохранить
    save_password_button = By.XPATH, './/button[text() = "Сохранить"]'
    # Кнопка Войти
    login_button = By.XPATH, './/a[text() = "Войти"]'