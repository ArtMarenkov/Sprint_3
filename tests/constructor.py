from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.locators import PagesLocators

class TestConstructor:

    def test_constructor_buns_select_success(self, driver_fixt, log_in_main_page):

        driver = driver_fixt
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.SAUCES)))
        driver.find_element(By.XPATH, PagesLocators.SAUCES).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located ((By.XPATH, PagesLocators.BUNS)))
        driver.find_element(By.XPATH, PagesLocators.BUNS).click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, PagesLocators.BUNS + '/..'), 'class', 'tab_tab_type_current'))
        assert "tab_tab_type_current" in driver.find_element(By.XPATH, PagesLocators.BUNS + '/..').get_attribute('class')

    def test_constructor_sauces_select_success(self, driver_fixt, log_in_main_page):

        driver = driver_fixt
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.SAUCES)))
        driver.find_element(By.XPATH, PagesLocators.SAUCES).click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, PagesLocators.SAUCES + '/..'), 'class', 'tab_tab_type_current'))
        assert "tab_tab_type_current" in driver.find_element(By.XPATH, PagesLocators.SAUCES + '/..').get_attribute('class')

    def test_constructor_filling_select_success(self, driver_fixt, log_in_main_page):

        driver = driver_fixt
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.FILLINGS)))
        driver.find_element(By.XPATH, PagesLocators.FILLINGS).click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, PagesLocators.FILLINGS + '/..'), 'class', 'tab_tab_type_current'))
        assert "tab_tab_type_current" in driver.find_element(By.XPATH, PagesLocators.FILLINGS + '/..').get_attribute('class')