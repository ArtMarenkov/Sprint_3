from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.locators import PagesLocators

class Test_Registration:

    def test_registration_new_user_success(self, driver_fixt, new_user_registration, get_mail, get_password):

        driver = driver_fixt
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.ENTER)))

        driver.find_element(By.CSS_SELECTOR, PagesLocators.LOGIN_FIELD).send_keys(get_mail)
        driver.find_element(By.CSS_SELECTOR, PagesLocators.PASS_FIELD).send_keys(get_password)

        driver.find_element(By.XPATH, PagesLocators.LOG_IN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.ASSEMBLE_LOGO)))
        driver.find_element(By.CSS_SELECTOR, PagesLocators.PERSONAL_ACC).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.ACC_TEXT)))
        assert "В этом разделе вы можете изменить свои персональные данные" == driver.find_element(By.XPATH, PagesLocators.ACC_TEXT).text

    def test_registration_password_error(self, driver_fixt, registration_form, get_name, get_mail):

        driver = driver_fixt
        driver.find_element(By.XPATH, PagesLocators.REG_NAME).send_keys(get_name)
        driver.find_element(By.XPATH, PagesLocators.REG_EMAIL).send_keys(get_mail)
        driver.find_element(By.XPATH, PagesLocators.REG_PASSWORD).send_keys('1')
        driver.find_element(By.XPATH, PagesLocators.REGISTER).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.WARNING)))
        assert 'Некорректный пароль' == driver.find_element(By.XPATH, PagesLocators.WARNING).text