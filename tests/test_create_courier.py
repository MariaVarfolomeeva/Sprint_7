import pytest
import requests
from utils.courier import register_new_courier_and_return_login_password


class TestCreateCourier:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field(self, missing_field):
        payload = {
            "login": "test_login",
            "password": "test_password",
            "firstName": "test_first_name"
        }
        payload.pop(missing_field)
        response = requests.post(self.BASE_URL, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    def test_create_courier_duplicate(self):
        courier_data = register_new_courier_and_return_login_password()
        payload = {
            "login": courier_data[0],
            "password": courier_data[1],
            "firstName": courier_data[2]
        }
        response = requests.post(self.BASE_URL, data=payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"

    def test_create_courier_success(self):
        courier_data = register_new_courier_and_return_login_password()
        assert len(courier_data) == 3
        response = requests.post(self.BASE_URL, data={
            "login": courier_data[0],
            "password": courier_data[1],
            "firstName": courier_data[2]
        })
        assert response.status_code == 201
        assert response.json() == {"ok": True}
