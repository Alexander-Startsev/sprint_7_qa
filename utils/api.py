import requests, time
import allure

BASE = "https://qa-scooter.praktikum-services.ru/api/v1"

def _send(method, url, **kwargs):
    kwargs.setdefault("timeout", 30)
    for i in range(2):
        try:
            return requests.request(method, url, **kwargs)
        except (requests.ReadTimeout, requests.ConnectionError):
            if i == 1:
                raise
            time.sleep(0.7)

@allure.step("POST {path}")
def post(path, *, json=None, data=None, params=None):
    return _send("POST", f"{BASE}{path}", json=json, data=data, params=params)

@allure.step("GET {path}")
def get(path, *, params=None):
    return _send("GET", f"{BASE}{path}", params=params)

@allure.step("DELETE {path}")
def delete(path):
    return _send("DELETE", f"{BASE}{path}")
