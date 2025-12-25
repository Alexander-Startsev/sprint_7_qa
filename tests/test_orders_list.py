import allure

@allure.feature("Orders")
class TestOrdersList:

    @allure.title("Список заказов возвращается (200) и содержит массив orders")
    def test_list_contains_orders(self, orders_api):
        r = orders_api.list()
        assert r.status_code == 200
        body = r.json()
        assert isinstance(body, dict)
        assert isinstance(body.get("orders"), list)
