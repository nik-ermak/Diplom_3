import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from data import FIREFOX_JS

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по кнопке')
    def click_on_element(self, locator):
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    @allure.step('Ожидание видимости элемента')
    def wait_for_element(self, locator, timeout= 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Получить текст одного элемента')
    def get_text_of_element(self, locator, timeout= 10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_all_elements_located(locator))
        return self.driver.find_element(*locator).text

    @allure.step('Получить текст нескольких элементов')
    def get_text_of_multiple_element(self, locator, timeout= 10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Проверить отображение элемента на дисплее')
    def checking_display_an_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Перетаскивание элемента')
    def drag_and_drop(self, first_element, second_element):
        if self.driver.name == 'firefox':
            ingredient = self.driver.find_element(*first_element)
            basket = self.driver.find_element(*second_element)
            self.driver.execute_script(FIREFOX_JS, ingredient, basket)
        else:
            ingredient = self.driver.find_element(*first_element)
            basket = self.driver.find_element(*second_element)
            ActionChains(self.driver).drag_and_drop(ingredient, basket).pause(3).perform()

    @allure.step('Ожидание кликабельности элемента')
    def wait_element_clickable(self, locator, timeout= 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Заполнение поля')
    def send_keys_to_input(self, locator, keys, timeout = 10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Элемент не отображается')
    def checking_element_not_displayed(self, locator, timeout= 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Передвижение к элементу и клик по нему')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()