import random


class UrlPage:
    URL = 'https://foodgram-frontend-1.prakticum-team.ru/recipes'
    LOG_URL = 'https://foodgram-frontend-1.prakticum-team.ru/signin'
    MAIN_URL = 'https://foodgram-frontend-1.prakticum-team.ru/recipes'



class GenUser:
    NAME = f"Рецептович{random.randint(1, 100000)}"
    LAST_NAME = f'Тестовый{random.randint(1, 100000)}'
    EMAIL = f'Testovoy{random.randint(1, 100000)}@ya.ru'
    PASSWORD = f'Ya{random.randint(100000, 1000000)}'




