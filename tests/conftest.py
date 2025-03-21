import pytest
import requests
from utils.courier import register_new_courier_and_return_login_password
from utils.urls import Urls

@pytest.fixture
def create_courier():
    """
    Фикстура для создания курьера и его удаления после теста.
    """
    courier_data = register_new_courier_and_return_login_password()
    yield courier_data

    payload = {
        "login": courier_data[0],
        "password": courier_data[1]
    }
    requests.post(Urls.LOGIN_URL, data=payload)
    requests.delete(f"{Urls.COURIER_URL}/{courier_data[0]}")