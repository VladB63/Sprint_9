import allure
from locators.reg_locators import RegLoc
from pages.base_page import BasePage
from data import GenUser


class RegPage(BasePage):

    @allure.step('Регистрация пользователя')
    def reg_new_user(self):
        self.add_text_to_element(RegLoc.NAME_INPUT, GenUser.NAME)
        self.add_text_to_element(RegLoc.LAST_NAME_INPUT, GenUser.LAST_NAME)
        self.add_text_to_element(RegLoc.USER_NAME_INPUT, GenUser.NAME)
        self.add_text_to_element(RegLoc.EMAIL_INPUT, GenUser.EMAIL)
        self.add_text_to_element(RegLoc.PASSWORD_INPUT, GenUser.PASSWORD)
        self.click_to_element(RegLoc.CREATE_BUTTON)
        return GenUser.EMAIL, GenUser.PASSWORD

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
