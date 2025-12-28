import pytest, allure
from utils.generator import courier as gen_courier

@allure.feature("Courier")
class TestCourierCreate:

    @allure.title("Можно создать курьера (201, ok=true)")
    def test_courier_can_be_created(self, courier_api, created_couriers):
        courier_payload = gen_courier()
        created_couriers.append(courier_payload)
        response = courier_api.create(courier_payload)
        assert response.status_code == 201
        response_json = response.json()
        assert isinstance(response_json, dict)
        assert response_json.get("ok") is True

    @allure.title("Нельзя создать двух одинаковых курьеров (409, есть message)")
    def test_cannot_create_same_twice(self, courier_api, created_couriers):
        courier_payload = gen_courier(login="same_login")
        created_couriers.append(courier_payload)
        courier_api.create(courier_payload)
        duplicate_response = courier_api.create(courier_payload)
        assert duplicate_response.status_code == 409
        response_json = duplicate_response.json()
        assert isinstance(response_json, dict)
        assert "message" in response_json

    @pytest.mark.parametrize("key", ["login", "password"], ids=["no_login","no_password"])
    @allure.title("Создание курьера без обязательного поля: {key} → 400 + message")
    def test_required_fields(self, courier_api, key):
        courier_payload = gen_courier()
        courier_payload.pop(key)
        response = courier_api.create(courier_payload)
        assert response.status_code == 400
        response_json = response.json()
        assert isinstance(response_json, dict) and "message" in response_json
