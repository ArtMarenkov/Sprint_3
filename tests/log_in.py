from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogIn:

    def test_log_in_by_personal_acc_success(self, login_data):

        login = login_data['login']
        password = login_data['password']

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, "//p[text() = 'Личный Кабинет']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'text']").send_keys(login)
        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'password']").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")))
        assert "Оформить заказ" == driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text

        driver.quit()

    def test_log_in__by_entry_button_success(self, login_data):
        login = login_data['login']
        password = login_data['password']
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'text']").send_keys(login)
        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'password']").send_keys(password)

        driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        driver.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']").click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "p[class='Account_text__fZAIn text text_type_main-default']")))

        assert "В этом разделе вы можете изменить свои персональные данные" == driver.find_element(By.CSS_SELECTOR, "p[class='Account_text__fZAIn text text_type_main-default']").text

        driver.quit()

    def test_log_in_by_registration_success(self, login_data):
        login = login_data['login']
        password = login_data['password']
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//a[@class = 'Auth_link__1fOlj' and text() = 'Зарегистрироваться']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//a[@class = 'Auth_link__1fOlj' and text() = 'Войти']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'text']").send_keys(login)
        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'password']").send_keys(password)

        driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        driver.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']").click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "p[class='Account_text__fZAIn text text_type_main-default']")))
        assert "В этом разделе вы можете изменить свои персональные данные" == driver.find_element(By.CSS_SELECTOR, "p[class='Account_text__fZAIn text text_type_main-default']").text

        driver.quit()

    def test_log_in_by_restore_password_success(self, login_data):

        login = login_data['login']
        password = login_data['password']

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//a[@class = 'Auth_link__1fOlj' and text() = 'Восстановить пароль']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//a[@class = 'Auth_link__1fOlj' and text() = 'Войти']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'text']").send_keys(login)
        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'password']").send_keys(password)

        driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        driver.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']").click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "p[class='Account_text__fZAIn text text_type_main-default']")))
        assert "В этом разделе вы можете изменить свои персональные данные" == driver.find_element(By.CSS_SELECTOR, "p[class='Account_text__fZAIn text text_type_main-default']").text

        driver.quit()