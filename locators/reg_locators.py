from selenium.webdriver.common.by import By

class RegLoc:

    NAME_INPUT = By.XPATH, '//div[text()="Имя"]/following-sibling::input[@name="first_name"]'
    LAST_NAME_INPUT = By.XPATH, '//div[text()="Фамилия"]/following-sibling::input[@name="last_name"]'
    USER_NAME_INPUT = By.XPATH, '//div[text()="Имя пользователя"]/following-sibling::input[@name="username"]'
    EMAIL_INPUT = By.XPATH, '//div[text()="Адрес электронной почты"]/following-sibling::input[@name="email"]'
    PASSWORD_INPUT = By.XPATH, '//div[text()="Пароль"]/following-sibling::input[@name="password"]'

    CREATE_BUTTON = By.XPATH, '//button[text()="Создать аккаунт"]'
    CREATE_BUTTON_DIS = By.XPATH, '//button[text()="Создать аккаунт" and @disabled]'

