import pytest
import requests


class TestCreateOrder:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/orders"

    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_different_colors(self, color):
        payload = {
            "firstName": "Тест",
            "lastName": "Тестов",
            "address": "Москва",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 5,
            "deliveryDate": "2023-10-10",
            "comment": "Тестовый заказ",
            "color": color
        }
        response = requests.post(self.BASE_URL, json=payload)
        assert response.status_code == 201
        assert "track" in response.json()
