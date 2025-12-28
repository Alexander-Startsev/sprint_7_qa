import pytest, allure

@allure.feature("Courier")
class TestCourierLogin:

    @allure.title("Курьер может авторизоваться (200, ответ содержит id)")
    def test_login_returns_id(self, courier_api, courier_data):
        r = courier_api.login({"login": courier_data["login"], "password": courier_data["password"]})
        assert r.status_code == 200
        j = r.json()
        assert isinstance(j.get("id"), int)

    @pytest.mark.parametrize("miss", ["login", "password"], ids=["no_login","no_password"])
    @allure.title("Логин без обязательного поля: {miss} → 400 + message")
    def test_login_missing_field(self, courier_api, miss):
        data = {"password": "x"} if miss == "login" else {"login": "x"}
        r = courier_api.login(data)
        assert r.status_code == 400
        j = r.json()
        assert isinstance(j, dict) and "message" in j

    @allure.title("Логин с неверным паролем → 404 + message")
    def test_login_wrong_password(self, courier_api, courier_data):
        r = courier_api.login({"login": courier_data["login"], "password": "wrong"})
        assert r.status_code == 404
        j = r.json()
        assert isinstance(j, dict) and "message" in j

    @allure.title("Логин несуществующего пользователя → 404 + message")
    def test_login_nonexistent(self, courier_api):
        r = courier_api.login({"login": "ghost_user", "password": "x"})
        assert r.status_code == 404
        j = r.json()
        assert isinstance(j, dict) and "message" in j
