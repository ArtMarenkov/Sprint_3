import random
from dataclasses import dataclass

@dataclass
class User:
    user_name: str
    user_email: str = 'marenkov_9@gmail.com'
    user_password: str = 'ko16pyth&81'

    def __init__(self, name, email, password):
        self.user_name = name
        self.user_email = email
        self.user_password = password

def get_user_data():

    reg_name = 'Ttester' + str(random.randint(1000, 999999999))
    reg_mail = f'{reg_name}' + '@gmail.com'
    reg_password = 'qwerty' + str(random.randint(1000, 999999999))

    user = User(reg_name, reg_mail, reg_password)

    return user