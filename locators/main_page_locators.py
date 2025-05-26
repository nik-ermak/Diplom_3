from selenium.webdriver.common.by import By

class LocatorsMainPage:
    # Шапка страницы
    # Кнопка конструктора
    constructor_button = By.XPATH, ".//p[contains(text(), 'Конструктор')]"
    # Кнопка Личный Кабинет
    personal_account_button = By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]"
    # Кнопка Лента заказов
    order_feed_button = By.XPATH, ".//p[contains(text(), 'Лента Заказов')]"

    # Основная часть
    # Кнопка Войти в аккаунт
    login_button = By.XPATH, './/button[text() = "Войти в аккаунт"]'
    # Форма конструктора бургера
    constructor_form = By.XPATH, './/div[@class = "BurgerIngredients_ingredients__menuContainer__Xu3Mo"]'
    # Заголовок раздела Конструктор
    constructor_title = By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1'
    # Заголовок раздела Булки в меню конструктора
    buns_block = By.XPATH, '//span[text() = "Булки"]'
    # Корзина куда перетаскиваются ингредиенты
    order_basket = By.XPATH, './/div[contains(@class, "constructor-element_pos_top")]'
    # Кнопка оформления заказа
    create_order_button = By.XPATH, ".//button[text() = 'Оформить заказ']"
    # Линк флюоресцентной булки
    fluorescent_bun_link = By.XPATH, './/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]'
    # Окно деталей ингредиента
    ingredient_details_window = By.XPATH, './/div[@class = "Modal_modal__contentBox__sCy8X pt-10 pb-15"]'
    # Заголовок окна "Детали ингредиента"
    header_of_ingredient_details = By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]'
    # Крестик в окне деталей ингредиента
    close_ingredient_details_button = By.XPATH, './/button[contains(@class,"close")]'
    # Счётчик количества ингредиентов
    counter_ingredient = By.XPATH, './/p[contains(@class, "counter_counter__num__3nue1")]'
    # Окно оформленного заказа
    window_created_order = By.XPATH, './/div[@class = "Modal_modal__container__Wo2l_"]'
    # Кнопка закрытия окна оформленного заказа
    close_button_created_order = By.XPATH, './/button[@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'
    # Номер заказа
    number_of_order = By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]"
    # Форма Ленты заказа
    order_feed_form = By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']"
    # Оверлей
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"