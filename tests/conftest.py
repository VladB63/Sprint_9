import pytest
from selenium import webdriver
from pages.reg_page import RegPage
from pages.recipe_page import RecipePage


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def new_user_registration(driver):
    rec_p = RecipePage(driver)
    rec_p.open_url()
    rec_p.click_to_create_button()
    rp = RegPage(driver)
    email, password = rp.reg_new_user()
    return email, password

