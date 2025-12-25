import pytest, allure
from utils.generator import courier as gen_courier

@allure.feature("Courier")
class TestCourierCreate:

    @allure.title("Можно создать курьера (201, ok=true)")
    def test_courier_can_be_created(self, courier_api):
        body = gen_courier()
        r = courier_api.create(body)
        assert r.status_code == 201
        j = r.json()
        assert isinstance(j, dict)
        assert j.get("ok") is True

    @allure.title("Нельзя создать двух одинаковых курьеров (409/400, есть message)")
    def test_cannot_create_same_twice(self, courier_api):
        body = gen_courier(login="same_login")
        courier_api.create(body)
        r = courier_api.create(body)
        assert r.status_code in (409, 400)
        j = r.json()
        assert isinstance(j, dict)
        assert "message" in j or j.get("ok") is False

    @pytest.mark.parametrize("key", ["login", "password"], ids=["no_login","no_password"])
    @allure.title("Создание курьера без обязательного поля: {key} → 400 + message")
    def test_required_fields(self, courier_api, key):
        body = gen_courier()
        body.pop(key)
        r = courier_api.create(body)
        assert r.status_code == 400
        j = r.json()
        assert isinstance(j, dict) and "message" in j
