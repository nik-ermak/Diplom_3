from selenium.webdriver.common.by import By


class LocatorsOrderFeed:
    # Заголовок страницы Лента заказов
    orders_list_title = By.XPATH, '//h1[text()="Лента заказов"]'
    # Окно детали заказа
    window_order_info = By.XPATH, '//p[text()= "Cостав"]'
    # Заказы В работе
    orders_in_progress = By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]"
    # Счётчик заказов выполненных за всё время
    list_total_orders = By.XPATH, './/p[text()="Выполнено за все время:"]/following-sibling::p'
    # Счётчик заказов выполненных за день
    list_daily_orders = By.XPATH, './/p[text()="Выполнено за сегодня:"]/following-sibling::p'
    # История всех заказов
    history_orders = By.XPATH, './/p[contains(@class, "text_type_digits-default")]'
    # Заказ в истории
    order_in_history = By.XPATH, './/li[contains(@class, "OrderHistory_listItem__2x95r")][1]'