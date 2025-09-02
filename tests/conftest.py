import pytest
from datetime import datetime


# Фикстуры для модуля masks
@pytest.fixture(
    params=[
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
    ]
)
def card_data(request):
    """Фикстура для тестов карт: (номер_карты, ожидаемый_результат)"""
    return request.param


@pytest.fixture(
    params=[
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
        ("1234", "**1234"),
    ]
)
def account_data(request):
    """Фикстура для тестов счетов: (номер_счета, ожидаемый_результат)"""
    return request.param


@pytest.fixture
def sample_operations():
    """Фикстура с примером списка операций для тестов"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-12-01T12:00:00.000000", "amount": 100},
        {"id": 2, "state": "PENDING", "date": "2023-11-15T09:30:00.000000", "amount": 200},
        {"id": 3, "state": "EXECUTED", "date": "2023-12-05T18:45:00.000000", "amount": 300},
        {"id": 4, "state": "CANCELED", "date": "2023-10-10T04:20:00.000000", "amount": 400},
        {"id": 5, "state": "EXECUTED", "date": "2023-12-01T12:00:00.000000", "amount": 500},
    ]


@pytest.fixture(params=["EXECUTED", "PENDING", "CANCELED"])
def state_filter(request):
    """Фикстура для параметризации по разным статусам"""
    return request.param


@pytest.fixture(
    params=[
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("МИР 1234567812345678", "МИР 1234 56** **** 5678"),
        ("MasterCard 1111222233334444", "MasterCard 1111 22** **** 4444"),
    ]
)
def account_card_data(request):
    """Фикстура для тестов mask_account_card"""
    return request.param


@pytest.fixture(
    params=[
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2021-12-31T23:59:59.999999", "31.12.2021"),
        ("2000-01-01T00:00:00.000000", "01.01.2000"),
        ("1999-12-31T00:00:00.000000", "31.12.1999"),
    ]
)
def date_data(request):
    """Фикстура для тестов get_date"""
    return request.param


@pytest.fixture(params=["", "2024-03-11", "invalid-date"])
def invalid_date_data(request):
    """Фикстура для некорректных данных get_date"""
    return request.param


# Добавляем к существующим фикстурам
@pytest.fixture
def sample_operations():
    """Фикстура с примером списка операций для тестов processing"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-12-01T12:00:00.000000", "amount": 100},
        {"id": 2, "state": "PENDING", "date": "2023-11-15T09:30:00.000000", "amount": 200},
        {"id": 3, "state": "EXECUTED", "date": "2023-12-05T18:45:00.000000", "amount": 300},
        {"id": 4, "state": "CANCELED", "date": "2023-10-10T04:20:00.000000", "amount": 400},
        {"id": 5, "state": "EXECUTED", "date": "2023-12-01T12:00:00.000000", "amount": 500},
    ]


@pytest.fixture
def operations_without_dates():
    """Фикстура с операциями без дат и с пустыми датами"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T12:00:00.000000"},
        {"id": 2, "state": "EXECUTED"},  # Нет даты
        {"id": 3, "state": "EXECUTED", "date": ""},  # Пустая дата
        {"id": 4, "state": "EXECUTED", "date": "2023-01-02T12:00:00.000000"},
    ]


@pytest.fixture(params=["EXECUTED", "PENDING", "CANCELED", "UNKNOWN"])
def state_filter(request):
    """Фикстура для параметризации по разным статусам"""
    return request.param


@pytest.fixture(params=[True, False])
def sort_direction(request):
    """Фикстура для параметризации направления сортировки"""
    return request.param
