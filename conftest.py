import pytest
import random

@pytest.fixture
def new_user_for_register():

    reg_name = 'Ttester' + str(random.randint(1000, 999999999))
    reg_mail = f'{reg_name}' + '@gmail.com'
    reg_password ='qwerty' + str(random.randint(1000, 999999999))

    return {"reg_name":reg_name, "reg_mail":reg_mail, "reg_password": reg_password}

@pytest.fixture
def login_data():

    login = "marenkov_9@gmail.com"
    password = "ko16pyth&81"

    return {"login":login, "password": password}