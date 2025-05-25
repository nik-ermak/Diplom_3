from selenium.webdriver.common.by import By


class LocatorsPersonalAccountPage:
    # Форма профиля
    personal_account_form = By.XPATH, './/div[@class = "Account_account__vgk_w"]'
    # Кнопка Профиль
    personal_account_button = By.XPATH, './/a[text() = "Профиль"]'
    # Кнопка История заказов
    history_orders_button = By.XPATH, './/a[text() = "История заказов"]'
    # Форма Истории заказов
    history_orders_form = By.XPATH, './/div[@class = "Account_contentBox__2CPm3"]'
    # Номер заказа
    number_order = By.XPATH, './/p[contains(@class, "text_type_digits-default")]'
    # Кнопка Сохранить
    save_button = By.XPATH, './/button[text() = "Сохранить"]'
    # Кнопка Отмена
    cansel_button = By.XPATH, './/button[text() = "Отмена"]'
    # Кнопка Выход
    logout_button = By.XPATH, './/button[text() = "Выход"]'