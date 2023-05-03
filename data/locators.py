
class PagesLocators:

    PERSONAL_ACC = "[href = '/account']"
    LOG_IN_ACC = "//button[text() = 'Войти в аккаунт']"
    REG_NAME = "//label[text() = 'Имя']/following-sibling:: input"
    REG_EMAIL = "//label[text() = 'Email']/following-sibling:: input"
    REG_PASSWORD = "//input[@name = 'Пароль']"
    LOGIN_FIELD = "input[name = 'name']"
    PASS_FIELD = "input[name = 'Пароль']"
    LOG_IN_BUTTON = "//button[text() = 'Войти']"
    TO_REGISTRATION_BUTTON = "//a[text() = 'Зарегистрироваться']"
    REGISTER = "//button[text() = 'Зарегистрироваться']"
    RESTORE = "//button[text() = 'Восстановить']"
    CONSTRUCTOR_BUTTON = "//p[text() = 'Конструктор']"
    LOGO_BUTTON = "div[class *= 'AppHeader_header']"
    BUNS = "//span[text()= 'Булки']"
    SAUCES = "//span[text()= 'Соусы']"
    FILLINGS = "//span[text()= 'Начинки']"
    LOGOUT_BUTTON = "//button[text() = 'Выход']"
    ACC_TEXT = "//p[text() = 'В этом разделе вы можете изменить свои персональные данные']"
    ENTER_BUTTON = "//a[text() = 'Войти']"
    RESTORE_PASS_BUTTON = "[href = '/forgot-password']"
    CHECKOUT_BUTTON = "//button[text() = 'Оформить заказ']"
    AUTH_FORM = "//div[h2 = 'Вход']"
    ENTER = "//h2[text() = 'Вход']"
    WARNING = "//p[text() = 'Некорректный пароль']"
    ASSEMBLE_LOGO = "//h1[text() = 'Соберите бургер']"