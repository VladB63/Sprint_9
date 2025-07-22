import allure
import pytest
from pages.auth_page import AuthPage
from pages.recipe_page import RecipePage


class TestRecipePage:

    @allure.step('Проверка создания рецепта')
    @pytest.mark.parametrize(
        "name,ingrit,massa,time,description,image_filename", [
            ('Вкусно и .', 'те', '500', '20', 'скажи сам что чувствуешь', 'Картинка.jpg')
        ]
    )
    def test_create_recipe(self, driver, new_user_registration,
                           name, ingrit, massa, time, description,
                           image_filename):
        email, password = new_user_registration
        rec_p = RecipePage(driver)
        ap = AuthPage(driver)
        ap.auth_user(email, password)
        ap.click_enter_button()
        rec_p.click_to_create_recipe()
        name_recipe = rec_p.add_field_recipe(name, ingrit, massa, time, description, image_filename)
        name_head = rec_p.get_text_head()
        rec_p.click_recipe_button()
        name_first_resipe = rec_p.get_text_first_head_recipe()
        assert name_recipe == name_head and name_recipe == name_first_resipe

