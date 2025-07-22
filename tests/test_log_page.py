import allure
import pytest
from data import GenUser, UrlPage
from pages.auth_page import AuthPage
from pages.recipe_page import RecipePage


class TestLogPage:

    @allure.step('Проверка авторизации пользователя')
    def test_log_user(self, driver, new_user_registration):
        email, password = new_user_registration
        rec_p = RecipePage(driver)
        ap = AuthPage(driver)
        ap.auth_user(email, password)
        ap.click_enter_button()
        exit_button = rec_p.find_exit_button()
        current_url = ap.get_current_url()
        assert current_url == UrlPage.MAIN_URL and exit_button.is_displayed()




    @allure.step('Проверка авторизации пользователя с не полными данными')
    @pytest.mark.parametrize(
        "email, password", [
            ('', GenUser.PASSWORD),
            (GenUser.EMAIL, ''),
            ('', '')
        ]
    )
    def test_log_user_failed(self, driver, email, password):
        rec_p = RecipePage(driver)
        rec_p.open_url()
        rec_p.click_to_enter_button()
        ap = AuthPage(driver)
        ap.auth_user(email, password)
        button_disabled = ap.disabled_enter_button()
        assert button_disabled.is_displayed()

