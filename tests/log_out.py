from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogOut:

    def test_log_out_from_personal_acc_success(self, login_data):

        login = login_data['login']
        password = login_data['password']

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, "//p[text() = 'Личный Кабинет']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'text']").send_keys(login)
        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'password']").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text() = 'Личный Кабинет']")))
        driver.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']").click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'Account_button__14Yp3 text text_type_main-medium text_color_inactive']")))
        driver.find_element(By.CSS_SELECTOR,"button[class = 'Account_button__14Yp3 text text_type_main-medium text_color_inactive']").click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "[class = 'Auth_login__3hAey']")))
        assert "Войти" ==  driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").text

        driver.quit()

