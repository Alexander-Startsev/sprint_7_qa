
import random, string
from datetime import datetime, timedelta

letters = string.ascii_lowercase

def rnd(n=10):
    return ''.join(random.choice(letters) for _ in range(n))

def courier(login=None, password=None, first_name=None):
    return {
        "login": login or rnd(),
        "password": password or rnd(12),
        "firstName": first_name or "Auto"
    }

def order(colors=None):
    return {
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "address": "Москва, Тверская 1",
        "metroStation": 4,
        "phone": "+7 999 111 22 33",
        "rentTime": 2,
        "deliveryDate": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
        "comment": "test",
        "color": colors or []
    }
