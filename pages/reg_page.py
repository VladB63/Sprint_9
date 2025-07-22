import allure
import random
from locators.reg_locators import RegLoc
from pages.base_page import BasePage


class RegPage(BasePage):

    @allure.step('Регистрация пользователя')
    def reg_new_user(self):
        NAME = f"Рецептович{random.randint(1, 100000)}"
        LAST_NAME = f'Тестовый{random.randint(1, 100000)}'
        EMAIL = f'Testovoy{random.randint(1, 100000)}@ya.ru'
        PASSWORD = f'Ya{random.randint(100000, 1000000)}'
        self.add_text_to_element(RegLoc.NAME_INPUT, NAME)
        self.add_text_to_element(RegLoc.LAST_NAME_INPUT, LAST_NAME)
        self.add_text_to_element(RegLoc.USER_NAME_INPUT, NAME)
        self.add_text_to_element(RegLoc.EMAIL_INPUT, EMAIL)
        self.add_text_to_element(RegLoc.PASSWORD_INPUT, PASSWORD)
        self.click_to_element(RegLoc.CREATE_BUTTON)
        return EMAIL, PASSWORD

    @allure.step('Регистрация пользователя с не полными данными')
    def reg_new_user_false(self, name, last_name, user_name, email, password):
        self.add_text_to_element(RegLoc.NAME_INPUT, name)
        self.add_text_to_element(RegLoc.LAST_NAME_INPUT, last_name)
        self.add_text_to_element(RegLoc.USER_NAME_INPUT, user_name)
        self.add_text_to_element(RegLoc.EMAIL_INPUT, email)
        self.add_text_to_element(RegLoc.PASSWORD_INPUT, password)


    @allure.step('Неактивная кнопка Создать аккаунт')
    def disabled_button_create(self):
        return self.find_element_with_wait(RegLoc.CREATE_BUTTON_DIS)
