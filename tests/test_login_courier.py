import pytest
import requests
import allure
from utils.courier import register_new_courier_and_return_login_password
from utils.urls import Urls


class TestLoginCourier:
    """
    Тесты для проверки функциональности входа курьера.
    """

    def test_login_courier_success(self):
        """
        Позитивный сценарий: успешный вход курьера.
        """
        courier_data = register_new_courier_and_return_login_password()
        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }
        response = requests.post(Urls.LOGIN_URL, data=payload)

        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert "id" in response.json(), "В ответе отсутствует поле 'id'"

    def test_login_courier_invalid_credentials(self):
        """
        Негативный сценарий: вход с неверными учетными данными.
        """
        payload = {
            "login": "invalid_login",
            "password": "invalid_password"
        }
        response = requests.post(Urls.LOGIN_URL, data=payload)

        assert response.status_code == 404, f"Ожидался код 404, но получен {response.status_code}"
        assert response.json()["message"] == "Учетная запись не найдена", \
            "Ожидалось сообщение 'Учетная запись не найдена'"

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_missing_field(self, missing_field):
        """
        Негативный сценарий: вход без обязательного поля.
        """
        payload = {
            "login": "test_login",
            "password": "test_password"
        }
        payload.pop(missing_field)
        response = requests.post(Urls.LOGIN_URL, data=payload)

        assert response.status_code == 400, f"Ожидался код 400, но получен {response.status_code}"
        assert response.json()["message"] == "Недостаточно данных для входа", \
            "Ожидалось сообщение 'Недостаточно данных для входа'"