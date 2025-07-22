import allure
from pathlib import Path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход по урлу')
    def go_to_url(self, url):
        self.driver.get(url)


    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()


    @allure.step('Ввод текста в поле')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение ссылки')
    def get_current_url(self):
        return self.driver.current_url


    @allure.step('Цикл для поиска локаторов')
    def verify_elements_displayed(self, locators):
        for locator in locators:
            element = self.find_element_with_wait(locator)
            return element

    @allure.step('Добавление файла')
    def get_image_path(self, filename):
        project_dir = Path(__file__).resolve().parent.parent
        image_path = project_dir / filename
        print(image_path)  # Для отладки
        return image_path


    @allure.step('Получить текст элемента')
    def giv_text_element(self, locator):
        return self.find_element_with_wait(locator).text