import pytest
from src.widget import mask_account_card, get_date


# Тесты для mask_account_card с фикстурами
def test_mask_account_card_with_fixture(account_card_data):
    """Тестируем mask_account_card с фикстурой"""
    input_data, expected = account_card_data
    assert mask_account_card(input_data) == expected


def test_mask_account_card_invalid_empty():
    """Тестируем пустые строки для mask_account_card - должны вызывать исключение"""
    with pytest.raises(ValueError, match="Получена пустая строка"):
        mask_account_card("")
    with pytest.raises(ValueError, match="Получена пустая строка"):
        mask_account_card("   ")


def test_mask_account_card_invalid_no_number():
    """Тестируем строки без номера - должны возвращать строку с ошибкой"""
    result = mask_account_card("TestWithoutNumber")
    assert "Ошибка" in result or result == "TestWithoutNumber"


# Тесты для get_date с фикстурами
def test_get_date_with_fixture(date_data):
    """Тестируем get_date с фикстурой"""
    input_date, expected = date_data
    assert get_date(input_date) == expected


def test_get_date_invalid(invalid_date_data):
    """Тестируем некорректные данные для get_date"""
    with pytest.raises(ValueError):
        get_date(invalid_date_data)


# Дополнительные тесты для полного покрытия
def test_mask_account_card_edge_cases():
    """Тестируем крайние случаи для mask_account_card"""
    # Короткие номера
    assert mask_account_card("Счет 1234") == "Счет **1234"
    assert mask_account_card("Card 1234567812345678") == "Card 1234 56** **** 5678"

    # С пробелами в номере - теперь ожидаем ошибку
    result = mask_account_card("Visa Platinum 7000 7922 8960 6361")
    assert "Ошибка" in result  # Ожидаем сообщение об ошибке


def test_get_date_edge_cases():
    """Тестируем крайние случаи для get_date"""
    # Разные форматы времени
    assert get_date("2024-03-11T00:00:00.000000") == "11.03.2024"
    assert get_date("2024-03-11T23:59:59.999999") == "11.03.2024"

    # Високосный год
    assert get_date("2024-02-29T12:00:00.000000") == "29.02.2024"


def test_mask_account_card_error_handling():
    """Тестируем обработку ошибок в mask_account_card"""
    # Номер карты с буквами
    result = mask_account_card("Visa Platinum 1234abcd5678efgh")
    assert "Ошибка" in result

    # Слишком короткий номер счета
    result = mask_account_card("Счет 123")
    assert "Ошибка" in result


# Параметризованные тесты
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa 0000000000000000", "Visa 0000 00** **** 0000"),
        ("Счет 00000000000000000000", "Счет **0000"),
    ],
)
def test_mask_account_card_parametrized(input_str, expected):
    """Тестируем mask_account_card с параметризацией"""
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2020-02-29T12:00:00.000000", "29.02.2020"),  # високосный
        ("2100-01-01T00:00:00.000000", "01.01.2100"),  # будущее
    ],
)
def test_get_date_parametrized(input_date, expected):
    """Тестируем get_date с параметризацией"""
    assert get_date(input_date) == expected


if __name__ == "__main__":
    pytest.main(["-v", __file__])
