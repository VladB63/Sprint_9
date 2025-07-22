from selenium.webdriver.common.by import By


class RecipeLoc:

    CREATE_AC_BUTTON = By.XPATH, '//a[@href="/signup"]'
    ENTER_BUTTON = By.XPATH, '//a[@href="/signin"]'
    EXIT_BUTTON = By.XPATH, '//a[text()="Выход"]'
    CREATE_RECIPE_TAB = By.XPATH, '//a[@href="/recipes/create" and text()="Создать рецепт"]'
    CREATE_RECIPE_BUTTON = By.XPATH, '//button[text()="Создать рецепт"]'


    NAME_RECIPE = By.XPATH, '//div[text()="Название рецепта"]/following-sibling::input[@class="styles_inputField__3eqTj"]'
    INGRIT_INPUT = By.XPATH, '//div[text()="Ингредиенты"]/following-sibling::input[@class="styles_inputField__3eqTj styles_ingredientsInput__1zzql"]'
    VOLUME_INPUT = By.XPATH, '//input[@class="styles_inputField__3eqTj styles_ingredientsAmountValue__2matT"]'
    ADD_INGRIT = By.XPATH, '//div[text()="Добавить ингредиент"]'
    TIME_PREPAR = By.XPATH, '//div[text()="Время приготовления"]/following-sibling::input[@class="styles_inputField__3eqTj"]'
    DESCRIPTION_RECIPE = By.XPATH, '//div[text()="Описание рецепта"]/following-sibling::textarea[@class="styles_textareaField__1wfhC"]'
    UPLOAD_FILE = By.XPATH, '//input[@type="file"]'
    TELYATINA_FARSH = By.XPATH, '//div[text()="телячий фарш"]'
    NAME_RECIPE_HEAD = By.XPATH, '//h1[@class="styles_single-card__title__2QMPq"]'
    NAME_FIRST_RECIPE = By.XPATH, '(//div[@class="style_card__body__3mEB4"])[1]//a[@class="style_link__1kPh8 style_card__title__1iaT0"]'
    RECIPE_TAB = By.XPATH, '//a[@href="/recipes" and text()="Рецепты"]'



