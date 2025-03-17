import pytest
import requests
from utils.courier import register_new_courier_and_return_login_password


@pytest.fixture
def create_courier():
    courier_data = register_new_courier_and_return_login_password()
    yield courier_data
    payload = {
        "login": courier_data[0],
        "password": courier_data[1]
    }
    requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)
    requests.delete(f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_data[0]}")
