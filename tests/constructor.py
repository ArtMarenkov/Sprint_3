from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructor:

    def test_constructor_buns_select_success(self, login_data):

        login = login_data['login']
        password = login_data['password']

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, "//p[text() = 'Личный Кабинет']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'text']").send_keys(login)
        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'password']").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Соусы']")))

        driver.find_element(By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Соусы']").click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Булки']")))
        driver.find_element(By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Булки']").click()

        assert "tab_tab_type_current" in  driver.find_element(By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Булки']/..").get_attribute('class')

        driver.quit()

    def test_constructor_sauces_select_success(self, login_data):

        login = login_data['login']
        password = login_data['password']

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, "//p[text() = 'Личный Кабинет']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'text']").send_keys(login)
        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'password']").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Соусы']")))

        driver.find_element(By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Соусы']").click()

        assert "tab_tab_type_current" in  driver.find_element(By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Соусы']/..").get_attribute('class')

        driver.quit()

    def test_constructor_filling_select_success(self, login_data):

        login = login_data['login']
        password = login_data['password']

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, "//p[text() = 'Личный Кабинет']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'text']").send_keys(login)
        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'password']").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Соусы']")))

        driver.find_element(By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Начинки']").click()

        assert "tab_tab_type_current" in  driver.find_element(By.XPATH, ".//span[@class = 'text text_type_main-default' and text() = 'Начинки']/..").get_attribute('class')

        driver.quit()