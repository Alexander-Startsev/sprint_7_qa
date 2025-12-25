import pytest, allure
from utils.generator import order as gen_order

@allure.feature("Orders")
class TestOrdersCreate:

    @pytest.mark.parametrize("colors", [
        pytest.param(["BLACK"], id="black"),
        pytest.param(["GREY"], id="grey"),
        pytest.param(["BLACK","GREY"], id="both"),
        pytest.param([], id="no_color"),
    ])
    @allure.title("Создать заказ (цвет: {colors}) → 201, ответ содержит track")
    def test_create_order(self, orders_api, created_order, colors):
        r = orders_api.create(gen_order(colors=colors))
        assert r.status_code == 201
        j = r.json()
        assert isinstance(j.get("track"), int)
        created_order.append(j["track"])
