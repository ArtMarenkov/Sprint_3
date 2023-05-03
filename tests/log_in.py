from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.locators import PagesLocators

class TestLogIn:

    def test_log_in_by_personal_acc_success(self, driver_fixt, log_in_main_page):

        driver = driver_fixt
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.CHECKOUT_BUTTON)))
        assert "Оформить заказ" == driver.find_element(By.XPATH, PagesLocators.CHECKOUT_BUTTON).text

    def test_log_in__by_entry_button_success(self, driver_fixt, login_existed, pass_existed):

        driver = driver_fixt
        driver.find_element(By.XPATH, PagesLocators.LOG_IN_ACC).click()

        driver.find_element(By.CSS_SELECTOR, PagesLocators.LOGIN_FIELD).send_keys(login_existed)
        driver.find_element(By.CSS_SELECTOR, PagesLocators.PASS_FIELD).send_keys(pass_existed)
        driver.find_element(By.XPATH, PagesLocators.LOG_IN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.CHECKOUT_BUTTON)))
        assert "Оформить заказ" == driver.find_element(By.XPATH, PagesLocators.CHECKOUT_BUTTON).text

    def test_log_in_by_registration_success(self, driver_fixt, login_existed, pass_existed):

        driver = driver_fixt
        driver.find_element(By.XPATH, PagesLocators.LOG_IN_ACC).click()

        driver.find_element(By.XPATH, PagesLocators.TO_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.REGISTER)))

        driver.find_element(By.XPATH, PagesLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.LOG_IN_BUTTON)))

        driver.find_element(By.CSS_SELECTOR, PagesLocators.LOGIN_FIELD).send_keys(login_existed)
        driver.find_element(By.CSS_SELECTOR, PagesLocators.PASS_FIELD).send_keys(pass_existed)
        driver.find_element(By.XPATH, PagesLocators.LOG_IN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.CHECKOUT_BUTTON)))
        assert "Оформить заказ" == driver.find_element(By.XPATH, PagesLocators.CHECKOUT_BUTTON).text

    def test_log_in_by_restore_password_success(self, driver_fixt, login_existed, pass_existed):

        driver = driver_fixt
        driver.find_element(By.XPATH, PagesLocators.LOG_IN_ACC).click()

        driver.find_element(By.CSS_SELECTOR, PagesLocators.RESTORE_PASS_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.RESTORE)))

        driver.find_element(By.XPATH, PagesLocators.ENTER_BUTTON).click()

        driver.find_element(By.CSS_SELECTOR, PagesLocators.LOGIN_FIELD).send_keys(login_existed)
        driver.find_element(By.CSS_SELECTOR, PagesLocators.PASS_FIELD).send_keys(pass_existed)
        driver.find_element(By.XPATH, PagesLocators.LOG_IN_BUTTON).click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.CHECKOUT_BUTTON)))
        assert "Оформить заказ" == driver.find_element(By.XPATH, PagesLocators.CHECKOUT_BUTTON).text