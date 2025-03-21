import pytest
import requests
import allure
from utils.courier import register_new_courier_and_return_login_password
from utils.data import ERROR_MESSAGES, SUCCESS_RESPONSES


class TestCreateCourier:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

    class TestCreateCourier:
        BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    @allure.title("Проверка создания курьера без обязательного поля: {missing_field}")
    def test_create_courier_missing_field(self, missing_field):
        """
        Негативный сценарий: попытка создать курьера без обязательного поля.
        Проверяет, что API возвращает статус 400 и корректное сообщение об ошибке.
        """
        payload = {
            "login": "test_login",
            "password": "test_password",
            "firstName": "test_first_name"
        }

        payload.pop(missing_field)

        response = requests.post(self.BASE_URL, data=payload)

        assert response.status_code == 400, f"Ожидался код 400, но получен {response.status_code}"

        assert response.json()["message"] == ERROR_MESSAGES["missing_field"], \
            f"Ожидалось сообщение '{ERROR_MESSAGES['missing_field']}', но получено {response.json()['message']}"

    def test_create_courier_success(self):
        """
        Позитивный сценарий: успешное создание курьера.
        """
        courier_data = register_new_courier_and_return_login_password()

        payload = {
            "login": courier_data[0],
            "password": courier_data[1],
            "firstName": courier_data[2]
        }
        response = requests.post(self.BASE_URL, data=payload)

        assert response.status_code == 201, f"Ожидался код 201, но получен {response.status_code}"

        assert response.json() == SUCCESS_RESPONSES["create_courier"], \
            f"Ожидался ответ {SUCCESS_RESPONSES['create_courier']}, но получен {response.json()}"

    def test_create_courier_duplicate(self):
        """
        Негативный сценарий: попытка создать курьера с уже существующим логином.
        """
        courier_data = register_new_courier_and_return_login_password()
        payload = {
            "login": courier_data[0],
            "password": courier_data[1],
            "firstName": courier_data[2]
        }
        response = requests.post(self.BASE_URL, data=payload)

        assert response.status_code == 409, f"Ожидался код 409, но получен {response.status_code}"

        assert response.json()["message"] == ERROR_MESSAGES["duplicate_login"], \
            f"Ожидалось сообщение '{ERROR_MESSAGES['duplicate_login']}', но получено {response.json()['message']}"

    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field(self, missing_field):
        """
        Негативный сценарий: попытка создать курьера без обязательного поля.
        """
        payload = {
            "login": "test_login",
            "password": "test_password",
            "firstName": "test_first_name"
        }
        payload.pop(missing_field)
        response = requests.post(self.BASE_URL, data=payload)

        assert response.status_code == 400, f"Ожидался код 400, но получен {response.status_code}"

        assert response.json()["message"] == ERROR_MESSAGES["missing_field"], \
            f"Ожидалось сообщение '{ERROR_MESSAGES['missing_field']}', но получено {response.json()['message']}"