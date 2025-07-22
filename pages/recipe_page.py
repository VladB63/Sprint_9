import allure
from locators.recipe_locators import RecipeLoc
from pages.base_page import BasePage
from data import UrlPage


class RecipePage(BasePage):

    @allure.step('Переход по урлу')
    def open_url(self):
        self.go_to_url(UrlPage.URL)

    @allure.step('Клик на кнопку Создать аккаунт')
    def click_to_create_button(self):
        self.click_to_element(RecipeLoc.CREATE_AC_BUTTON)


    @allure.step('Клик на кнопку Войти')
    def click_to_enter_button(self):
        self.click_to_element(RecipeLoc.ENTER_BUTTON)

    @allure.step('Клик на кнопку Рецепты')
    def click_recipe_button(self):
        self.click_to_element(RecipeLoc.RECIPE_TAB)


    @allure.step('Поиск кнопки выход')
    def find_exit_button(self):
        return self.find_element_with_wait(RecipeLoc.EXIT_BUTTON)

    @allure.step('Клик кнопки создать рецепт')
    def click_to_create_recipe(self):
        self.click_to_element(RecipeLoc.CREATE_RECIPE_TAB)


    @allure.step('Заполнение полей рецепта')
    def add_field_recipe(self, name, ingrit, massa, time, description, image_filename):
        self.add_text_to_element(RecipeLoc.NAME_RECIPE, name)
        self.add_text_to_element(RecipeLoc.INGRIT_INPUT, ingrit)
        self.click_to_element(RecipeLoc.TELYATINA_FARSH)
        self.add_text_to_element(RecipeLoc.VOLUME_INPUT, massa)
        self.click_to_element(RecipeLoc.ADD_INGRIT)
        self.add_text_to_element(RecipeLoc.TIME_PREPAR, time)
        self.add_text_to_element(RecipeLoc.DESCRIPTION_RECIPE, description)
        image_path = self.get_image_path(image_filename)
        self.driver.find_element(*RecipeLoc.UPLOAD_FILE).send_keys(str(image_path))
        self.click_to_element(RecipeLoc.CREATE_RECIPE_BUTTON)
        return name

    @allure.step('Получение текста заголовка')
    def get_text_head(self):
        return self.giv_text_element(RecipeLoc.NAME_RECIPE_HEAD)


    @allure.step('Получение первого заголовка на странице')
    def get_text_first_head_recipe(self):
        return self.giv_text_element(RecipeLoc.NAME_FIRST_RECIPE)




