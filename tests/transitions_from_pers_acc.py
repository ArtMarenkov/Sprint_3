from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestTransFromPersonalAcc:

    def test_transition_to_constructor_success(self, login_data):

        login = login_data['login']
        password = login_data['password']

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, "//p[text() = 'Личный Кабинет']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'text']").send_keys(login)
        driver.find_element(By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @type = 'password']").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        driver.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']").click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "p[class='Account_text__fZAIn text text_type_main-default']")))

        driver.find_elements(By.CSS_SELECTOR, "a[class = 'AppHeader_header__link__3D_hX']")[0].click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "h1[class = 'text text_type_main-large mb-5 mt-10']")))
        assert "Соберите бургер" == driver.find_element(By.CSS_SELECTOR,"h1[class = 'text text_type_main-large mb-5 mt-10']").text

        driver.quit()

    def test_transition_to_constructor_by_logo_success(self, login_data):

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

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[class = 'AppHeader_header__logo__2D0X2']")))
        driver.find_element(By.CSS_SELECTOR, "div[class = 'AppHeader_header__logo__2D0X2']").click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "h1[class = 'text text_type_main-large mb-5 mt-10']")))
        assert "Соберите бургер" == driver.find_element(By.CSS_SELECTOR,"h1[class = 'text text_type_main-large mb-5 mt-10']").text

        driver.quit()