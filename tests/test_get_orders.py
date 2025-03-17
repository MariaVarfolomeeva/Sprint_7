import requests


class TestGetOrders:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/orders"

    def test_get_orders_list(self):
        response = requests.get(self.BASE_URL)
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)
