
# Sprint_7 — API тесты «Яндекс Самокат»

## Установка
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск тестов и Allure
```bash
pytest -v -s --alluredir=allure-results
allure serve allure-results
```
