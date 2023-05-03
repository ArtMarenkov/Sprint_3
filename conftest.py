import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.random import get_random_data
from data.locators import PagesLocators
from selenium.webdriver.common.by import By

@pytest.fixture
def login_existed():
    return "marenkov_9@gmail.com"

@pytest.fixture
def pass_existed():
    return "ko16pyth&81"

@pytest.fixture
def driver_fixt():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    yield driver
    driver.quit()

@pytest.fixture
def get_name():
    reg_name = get_random_data('Ttester')
    return reg_name

@pytest.fixture
def get_mail(get_name):
    reg_mail = get_name + '@gmail.com'
    return reg_mail

@pytest.fixture
def get_password():
    reg_password = get_random_data('qwerty')
    return reg_password

@pytest.fixture
def log_in_main_page(driver_fixt, login_existed, pass_existed):
    driver = driver_fixt
    driver.find_element(By.CSS_SELECTOR, PagesLocators.PERSONAL_ACC).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.LOG_IN_BUTTON)))
    driver.find_element(By.CSS_SELECTOR, PagesLocators.LOGIN_FIELD).send_keys(login_existed)
    driver.find_element(By.CSS_SELECTOR, PagesLocators.PASS_FIELD).send_keys(pass_existed)
    driver.find_element(By.XPATH, PagesLocators.LOG_IN_BUTTON).click()

@pytest.fixture
def log_in_personal_cabinet(driver_fixt, log_in_main_page):
    driver = driver_fixt
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.ASSEMBLE_LOGO)))
    driver.find_element(By.CSS_SELECTOR, PagesLocators.PERSONAL_ACC).click()

@pytest.fixture
def registration_form(driver_fixt):
    driver = driver_fixt
    driver.find_element(By.CSS_SELECTOR, PagesLocators.PERSONAL_ACC).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.LOG_IN_BUTTON)))
    driver.find_element(By.XPATH, PagesLocators.TO_REGISTRATION_BUTTON).click()

@pytest.fixture
def new_user_registration(driver_fixt, get_name, get_mail, get_password):
    driver = driver_fixt
    driver.find_element(By.CSS_SELECTOR, PagesLocators.PERSONAL_ACC).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.LOG_IN_BUTTON)))
    driver.find_element(By.XPATH, PagesLocators.TO_REGISTRATION_BUTTON).click()
    driver.find_element(By.XPATH, PagesLocators.REG_NAME).send_keys(get_name)
    driver.find_element(By.XPATH, PagesLocators.REG_EMAIL).send_keys(get_mail)
    driver.find_element(By.XPATH, PagesLocators.REG_PASSWORD).send_keys(get_password)
    driver.find_element(By.XPATH, PagesLocators.REGISTER).click()