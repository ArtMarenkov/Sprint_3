import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.locators import PagesLocators
from selenium.webdriver.common.by import By
from data.data import User

@pytest.fixture
def driver_fixt():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    yield driver
    driver.quit()

@pytest.fixture
def log_in_main_page(driver_fixt):
    driver = driver_fixt
    driver.find_element(By.CSS_SELECTOR, PagesLocators.PERSONAL_ACC).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.LOG_IN_BUTTON)))
    driver.find_element(By.CSS_SELECTOR, PagesLocators.LOGIN_FIELD).send_keys(User.user_email)
    driver.find_element(By.CSS_SELECTOR, PagesLocators.PASS_FIELD).send_keys(User.user_password)
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