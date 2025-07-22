import allure
from locators.auth_locators import AuthLoc
from pages.base_page import BasePage


class AuthPage(BasePage):

    @allure.step('Авторизация пользователя')
    def auth_user(self, email, password):
        self.add_text_to_element(AuthLoc.EMAIL_INPUT, email)
        self.add_text_to_element(AuthLoc.PASSWORD_INPUT, password)


    @allure.step('Клик кнопки войти')
    def click_enter_button(self):
        self.click_to_element(AuthLoc.ENTER_BUTTON)


    @allure.step('Заголовок авторизации')
    def find_auth_header(self):
        return self.find_element_with_wait(AuthLoc.HEADER_LOGIN)


    @allure.step('Неактивная кнопка Войти')
    def disabled_enter_button(self):
        return self.find_element_with_wait(AuthLoc.ENTER_BUTTON_DIS)

