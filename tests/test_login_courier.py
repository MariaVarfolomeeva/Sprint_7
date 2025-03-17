import pytest
import requests
from utils.courier import register_new_courier_and_return_login_password


class TestLoginCourier:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier/login"

    def test_login_courier_success(self):
        courier_data = register_new_courier_and_return_login_password()
        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }
        response = requests.post(self.BASE_URL, data=payload)
        assert response.status_code == 200
        assert "id" in response.json()

    def test_login_courier_invalid_credentials(self):
        payload = {
            "login": "invalid_login",
            "password": "invalid_password"
        }
        response = requests.post(self.BASE_URL, data=payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_missing_field(self, missing_field):
        payload = {
            "login": "test_login",
            "password": "test_password"
        }
        payload.pop(missing_field)
        response = requests.post(self.BASE_URL, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"
