from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.locators import PagesLocators
from data.data import get_user_data

class Test_Registration:

    def test_registration_new_user_success(self, driver_fixt, registration_form):

        driver = driver_fixt
        new_user = get_user_data()
        driver.find_element(By.XPATH, PagesLocators.REG_NAME).send_keys(new_user.user_name)
        driver.find_element(By.XPATH, PagesLocators.REG_EMAIL).send_keys(new_user.user_email)
        driver.find_element(By.XPATH, PagesLocators.REG_PASSWORD).send_keys(new_user.user_password)
        driver.find_element(By.XPATH, PagesLocators.REGISTER).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.ENTER)))

        driver.find_element(By.CSS_SELECTOR, PagesLocators.LOGIN_FIELD).send_keys(new_user.user_email)
        driver.find_element(By.CSS_SELECTOR, PagesLocators.PASS_FIELD).send_keys(new_user.user_password)

        driver.find_element(By.XPATH, PagesLocators.LOG_IN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.ASSEMBLE_LOGO)))
        driver.find_element(By.CSS_SELECTOR, PagesLocators.PERSONAL_ACC).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.ACC_TEXT)))
        assert "В этом разделе вы можете изменить свои персональные данные" == driver.find_element(By.XPATH, PagesLocators.ACC_TEXT).text

    def test_registration_password_error(self, driver_fixt, registration_form):

        driver = driver_fixt
        new_user = get_user_data()
        driver.find_element(By.XPATH, PagesLocators.REG_NAME).send_keys(new_user.user_name)
        driver.find_element(By.XPATH, PagesLocators.REG_EMAIL).send_keys(new_user.user_password)
        driver.find_element(By.XPATH, PagesLocators.REG_PASSWORD).send_keys('1')
        driver.find_element(By.XPATH, PagesLocators.REGISTER).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.WARNING)))
        assert 'Некорректный пароль' == driver.find_element(By.XPATH, PagesLocators.WARNING).text