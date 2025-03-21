import requests
from utils.generators import generate_random_string


def register_new_courier_and_return_login_password():
    """
    Регистрирует нового курьера и возвращает его логин, пароль и имя.
    :return: Список [логин, пароль, имя], если регистрация успешна. Иначе пустой список.
    """
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        return [login, password, first_name]
    else:
        return []