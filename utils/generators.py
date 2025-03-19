import random
import string
from datetime import datetime, timedelta


def generate_random_string(length):
    """
    Генерирует случайную строку из букв нижнего регистра.
    :param length: Длина строки.
    :return: Случайная строка.
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_number(min_value=1, max_value=100):
    """
    Генерирует случайное число в заданном диапазоне.
    :param min_value: Минимальное значение (по умолчанию 1).
    :param max_value: Максимальное значение (по умолчанию 100).
    :return: Случайное число.
    """
    return random.randint(min_value, max_value)


def generate_random_email(domain="example.com"):
    """
    Генерирует случайный email.
    :param domain: Домен email (по умолчанию "example.com").
    :return: Случайный email.
    """
    username = generate_random_string(10)
    return f"{username}@{domain}"


def generate_random_phone():
    """
    Генерирует случайный номер телефона в формате +7XXXXXXXXXX.
    :return: Случайный номер телефона.
    """
    return f"+7{random.randint(1000000000, 9999999999)}"


def generate_random_date(start_date="2020-01-01", end_date="2023-12-31"):
    """
    Генерирует случайную дату в заданном диапазоне.
    :param start_date: Начальная дата (по умолчанию "2020-01-01").
    :param end_date: Конечная дата (по умолчанию "2023-12-31").
    :return: Случайная дата в формате YYYY-MM-DD.
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    random_date = start + timedelta(days=random.randint(0, (end - start).days))
    return random_date.strftime("%Y-%m-%d")


def generate_random_boolean():
    """
    Генерирует случайное булево значение (True или False).
    :return: Случайное булево значение.
    """
    return random.choice([True, False])
