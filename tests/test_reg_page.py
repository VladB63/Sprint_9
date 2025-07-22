import allure
import pytest
from data import GenUser, UrlPage
from pages.reg_page import RegPage
from pages.auth_page import AuthPage
from pages.recipe_page import RecipePage
from locators.auth_locators import AuthLoc


class TestAuthLogPage:


    @allure.step('Проверка регистрации нового пользователя')
    def test_reg_new_user(self, driver, new_user_registration):
        ap = AuthPage(driver)
        ap.find_auth_header()
        current_url = ap.get_current_url()
        auth_form = [
            AuthLoc.EMAIL_INPUT,
            AuthLoc.PASSWORD_INPUT,
            AuthLoc.ENTER_BUTTON]
        element = ap.verify_elements_displayed(auth_form)
        assert current_url == UrlPage.LOG_URL and element.is_displayed()


    @allure.step('Проверка регистрации нового пользователя с не полными данными')
    @pytest.mark.parametrize(
        "name, last_name, user_name, email, password", [
            ('', GenUser.LAST_NAME, GenUser.NAME, GenUser.EMAIL, GenUser.PASSWORD),
            (GenUser.NAME, '', GenUser.NAME, GenUser.EMAIL, GenUser.PASSWORD),
            (GenUser.NAME, GenUser.LAST_NAME, '', GenUser.EMAIL, GenUser.PASSWORD),
            (GenUser.NAME, GenUser.LAST_NAME, GenUser.NAME, '', GenUser.PASSWORD),
            (GenUser.NAME, GenUser.LAST_NAME, GenUser.NAME, GenUser.EMAIL, '')
        ]
    )
    def test_reg_new_user_failed(self, driver, name, last_name, user_name, email, password):
        rec_p = RecipePage(driver)
        rec_p.open_url()
        rec_p.click_to_create_button()
        rp = RegPage(driver)
        rp.reg_new_user_false(name, last_name, user_name, email, password)
        button_disabled = rp.disabled_button_create()
        assert button_disabled.is_displayed()


