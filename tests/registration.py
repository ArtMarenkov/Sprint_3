from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Test_Registration:

    def test_registration_new_user_success(self, new_user_for_register):
        reg_name = new_user_for_register['reg_name']
        reg_mail = new_user_for_register['reg_mail']
        reg_password = new_user_for_register['reg_password']

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//a[@class = 'Auth_link__1fOlj' and text() = 'Зарегистрироваться']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "input[class = 'text input__textfield text_type_main-default']")))

        driver.find_elements(By.CSS_SELECTOR, "[class = 'text input__textfield text_type_main-default']")[0].send_keys(reg_name)
        driver.find_elements(By.CSS_SELECTOR, "[class = 'text input__textfield text_type_main-default']")[1].send_keys(reg_mail)
        driver.find_elements(By.CSS_SELECTOR, "[class = 'text input__textfield text_type_main-default']")[2].send_keys(reg_password)

        driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text() = 'Вход']")))

        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'text']").send_keys(reg_mail)
        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'password']").send_keys(reg_password)

        driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text() = 'Личный Кабинет']")))
        driver.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "p[class='Account_text__fZAIn text text_type_main-default']")))

        assert "В этом разделе вы можете изменить свои персональные данные" == driver.find_element(By.CSS_SELECTOR, "p[class='Account_text__fZAIn text text_type_main-default']").text

        driver.quit()

    def test_registration_password_error(self, new_user_for_register):

        reg_name = new_user_for_register['reg_name']
        reg_mail = new_user_for_register['reg_mail']
        reg_password = '1'

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//a[@class = 'Auth_link__1fOlj' and text() = 'Зарегистрироваться']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "input[class = 'text input__textfield text_type_main-default']")))

        driver.find_elements(By.CSS_SELECTOR, "[class = 'text input__textfield text_type_main-default']")[0].send_keys(reg_name)
        driver.find_elements(By.CSS_SELECTOR, "[class = 'text input__textfield text_type_main-default']")[1].send_keys(reg_mail)
        driver.find_elements(By.CSS_SELECTOR, "[class = 'text input__textfield text_type_main-default']")[2].send_keys(reg_password)
        driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert 'Некорректный пароль' == driver.find_element(By.CSS_SELECTOR, "p[class = 'input__error text_type_main-default']").text