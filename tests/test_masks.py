import pytest
from src.masks import get_mask_card_number, get_mask_account


# Тесты с использованием фикстур
def test_get_mask_card_number_with_fixture(card_data):
    """Тестируем маскировку карт с фикстурой"""
    card_number, expected = card_data
    assert get_mask_card_number(card_number) == expected


def test_get_mask_account_with_fixture(account_data):
    """Тестируем маскировку счетов с фикстурой"""
    account_number, expected = account_data
    assert get_mask_account(account_number) == expected


# Тесты для полного покрытия
def test_get_mask_card_number_valid():
    """Тестируем корректные номера карт"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"


def test_get_mask_card_number_invalid():
    """Тестируем некорректные номера карт"""
    with pytest.raises(ValueError):
        get_mask_card_number("123456789")
    with pytest.raises(ValueError):
        get_mask_card_number("1234abcd5678efgh")


def test_get_mask_account_valid():
    """Тестируем корректные номера счетов"""
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("12345678901234567890") == "**7890"


def test_get_mask_account_invalid():
    """Тестируем некорректные номера счетов"""
    with pytest.raises(ValueError):
        get_mask_account("123")
    with pytest.raises(ValueError):
        get_mask_account("12ab")


def test_get_mask_card_number_edge_cases():
    """Тестируем крайние случаи для карт"""
    # Тестируем пустую строку
    with pytest.raises(ValueError):
        get_mask_card_number("")

    # Тестируем строку только с пробелами
    with pytest.raises(ValueError):
        get_mask_card_number("    ")

    # Тестируем номер с символами
    with pytest.raises(ValueError):
        get_mask_card_number("1234-5678-9012-3456")


def test_get_mask_account_edge_cases():
    """Тестируем крайние случаи для счетов"""
    # Тестируем пустую строку
    with pytest.raises(ValueError):
        get_mask_account("")

    # Тестируем строку только с пробелами
    with pytest.raises(ValueError):
        get_mask_account("    ")

    # Тестируем номер с символами
    with pytest.raises(ValueError):
        get_mask_account("1234-5678-9012")


def test_get_mask_card_number_exact_16_digits():
    """Тестируем точную длину 16 цифр"""
    # Граничный случай - ровно 16 цифр
    assert get_mask_card_number("0000000000000000") == "0000 00** **** 0000"


def test_get_mask_account_minimum_length():
    """Тестируем минимальную длину счета"""
    # Граничный случай - ровно 4 цифры
    assert get_mask_account("0000") == "**0000"
