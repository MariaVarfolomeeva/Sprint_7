# Sprint 7: Тестирование API для сервиса Scooter

Этот проект представляет собой набор автотестов для API сервиса Scooter. Тесты написаны на Python с использованием библиотек `pytest`, `requests` и `allure-pytest` для создания отчётов.


## Установка и настройка

1. **Клонирование репозитория**:
git clone https://github.com/MariaVarfolomeeva/Sprint_7.git
2. **Создание виртуальное окружения**:
python -m venv venv
3. **Активирование виртуального окружения**:
venv\Scripts\activate
4. **Установка зависимостей**:
pip install -r requirements.txt


## Запуск тестов
1. **Запустите тесты**:
pytest --alluredir=./target/allure-results

2. **Сгенерируйте отчёт Allure**:
allure serve ./target/allure-results

## Зависимости

pytest==6.2.5

requests==2.32.3

allure-pytest==2.32.2