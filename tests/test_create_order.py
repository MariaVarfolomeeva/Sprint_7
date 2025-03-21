import pytest
import requests
import allure
from utils.urls import Urls


class TestCreateOrder:
    """
    Тесты для проверки функциональности создания заказа.
    """

    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_different_colors(self, color):
        """
        Проверка создания заказа с разными цветами.
        """
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
        response = requests.post(Urls.ORDERS_URL, json=payload)

        assert response.status_code == 201, f"Ожидался код 201, но получен {response.status_code}"
        assert "track" in response.json(), "В ответе отсутствует поле 'track'"