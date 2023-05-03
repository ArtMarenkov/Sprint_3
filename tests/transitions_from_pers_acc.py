from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.locators import PagesLocators

class TestTransFromPersonalAcc:

    def test_transition_to_constructor_success(self, driver_fixt, log_in_personal_cabinet):

        driver = driver_fixt
        driver.find_element(By.XPATH, PagesLocators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.ASSEMBLE_LOGO)))
        assert "Соберите бургер" == driver.find_element(By.XPATH, PagesLocators.ASSEMBLE_LOGO).text

    def test_transition_to_constructor_by_logo_success(self, driver_fixt, log_in_personal_cabinet):

        driver = driver_fixt
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, PagesLocators.LOGO_BUTTON)))
        driver.find_element(By.CSS_SELECTOR, PagesLocators.LOGO_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH , PagesLocators.ASSEMBLE_LOGO)))
        assert "Соберите бургер" == driver.find_element(By.XPATH, PagesLocators.ASSEMBLE_LOGO).text