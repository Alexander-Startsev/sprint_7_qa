import requests
import allure
from .api import BASE

class CourierApi:
    def __init__(self):
        self.s = requests.Session()
        self.base = BASE

    @allure.step("Создать курьера")
    def create(self, data: dict):
        return self.s.post(f"{self.base}/courier", data=data, timeout=30)

    @allure.step("Логин курьера")
    def login(self, data: dict):
        return self.s.post(f"{self.base}/courier/login", data=data, timeout=30)

    @allure.step("Удалить курьера #{courier_id}")
    def delete(self, courier_id: int):
        return self.s.delete(f"{self.base}/courier/{courier_id}", timeout=30)


class OrdersApi:
    def __init__(self):
        self.s = requests.Session()
        self.base = BASE

    @allure.step("Создать заказ")
    def create(self, body: dict):
        return self.s.post(f"{self.base}/orders", json=body, timeout=30)

    @allure.step("Отменить заказ, трек={track}")
    def cancel(self, track: int):
        return self.s.post(f"{self.base}/orders/cancel", json={"track": track}, timeout=30)

    @allure.step("Получить список заказов")
    def list(self, params: dict | None = None):
        return self.s.get(f"{self.base}/orders", params=params, timeout=30)
