from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.locators import PagesLocators

class TestPersonalAcc:

    def test_personal_acc_success(self, driver_fixt, log_in_personal_cabinet):

        driver = driver_fixt
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, PagesLocators.ACC_TEXT)))
        assert "В этом разделе вы можете изменить свои персональные данные" == driver.find_element(By.XPATH, PagesLocators.ACC_TEXT).text