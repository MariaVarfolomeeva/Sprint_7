import requests
from utils.urls import Urls


class TestGetOrders:
    """
    Тесты для проверки функциональности получения списка заказов.
    """

    def test_get_orders_list(self):
        """
        Проверка получения списка заказов.
        """
        response = requests.get(Urls.ORDERS_URL)

        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert isinstance(response.json()["orders"], list), "Ответ не содержит списка заказов"
