from selenium.webdriver.common.by import By


class AuthLoc:

    EMAIL_INPUT = By.XPATH, '//div[text()="Электронная почта"]/following-sibling::input[@name="email"]'
    PASSWORD_INPUT = By.XPATH, '//div[text()="Пароль"]/following-sibling::input[@name="password"]'
    ENTER_BUTTON = By.XPATH, '//button[text()="Войти"]'
    ENTER_BUTTON_DIS = By.XPATH, '//button[text()="Войти" and @disabled]'

    HEADER_LOGIN = By.XPATH, '//h1[text()="Войти на сайт"]'

