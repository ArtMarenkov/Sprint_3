from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.locators import PagesLocators

class TestLogOut:

    def test_log_out_from_personal_acc_success(self, driver_fixt, log_in_personal_cabinet):

        driver = driver_fixt
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.LOGOUT_BUTTON)))
        driver.find_element(By.XPATH, PagesLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.AUTH_FORM)))
        assert "Войти" ==  driver.find_element(By.XPATH, PagesLocators.LOG_IN_BUTTON).text

