import pytest
from src.processing import filter_by_state, sort_by_date


# Тесты для filter_by_state с фикстурами
def test_filter_by_state_with_fixture(sample_operations, state_filter):
    """Тестируем filter_by_state с фикстурой разных статусов"""
    result = filter_by_state(sample_operations, state_filter)

    # Проверяем, что все элементы в результате имеют нужный статус
    if state_filter in ["EXECUTED", "PENDING", "CANCELED"]:
        assert all(item["state"] == state_filter for item in result)
    else:
        # Для неизвестного статуса должен вернуть пустой список
        assert result == []


def test_filter_by_state_default(sample_operations):
    """Тестируем filter_by_state со значением по умолчанию (EXECUTED)"""
    result = filter_by_state(sample_operations)
    assert all(item["state"] == "EXECUTED" for item in result)
    assert len(result) == 3  # Должно быть 3 EXECUTED операции


def test_filter_by_state_empty_list():
    """Тестируем filter_by_state с пустым списком"""
    assert filter_by_state([]) == []
    assert filter_by_state([], "EXECUTED") == []


def test_filter_by_state_no_state_field():
    """Тестируем filter_by_state с элементами без поля state"""
    data = [
        {"id": 1, "date": "2023-01-01T12:00:00.000000"},
        {"id": 2, "state": "EXECUTED", "date": "2023-01-02T12:00:00.000000"},
        {"id": 3, "date": "2023-01-03T12:00:00.000000"},
    ]
    result = filter_by_state(data, "EXECUTED")
    assert len(result) == 1
    assert result[0]["id"] == 2


# Тесты для sort_by_date с фикстурами
def test_sort_by_date_with_fixture(sample_operations, sort_direction):
    """Тестируем sort_by_date с фикстурой направлений сортировки"""
    result = sort_by_date(sample_operations, sort_direction)

    # Проверяем, что список отсортирован
    dates = [item["date"] for item in result if "date" in item]
    if len(dates) > 1:
        if sort_direction:  # reverse=True (убывание)
            assert dates == sorted(dates, reverse=True)
        else:  # reverse=False (возрастание)
            assert dates == sorted(dates)


def test_sort_by_date_default(sample_operations):
    """Тестируем sort_by_date со значением по умолчанию (reverse=True)"""
    result = sort_by_date(sample_operations)
    dates = [item["date"] for item in result if "date" in item]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_empty_list():
    """Тестируем sort_by_date с пустым списком"""
    assert sort_by_date([]) == []
    assert sort_by_date([], False) == []


def test_sort_by_date_without_dates(operations_without_dates):
    """Тестируем sort_by_date с операциями без дат"""
    result = sort_by_date(operations_without_dates)

    # Элементы без даты должны быть в конце (при reverse=True)
    assert result[0]["id"] == 4  # Самая поздняя дата
    assert result[1]["id"] == 1  # Более ранняя дата
    # Элементы без даты - в конце
    assert result[2]["id"] in [2, 3]
    assert result[3]["id"] in [2, 3]


def test_sort_by_date_identical_dates(sample_operations):
    """Тестируем sort_by_date с одинаковыми датами"""
    # Добавляем операцию с такой же датой как у существующей
    duplicate_date_operation = {"id": 6, "state": "EXECUTED", "date": "2023-12-01T12:00:00.000000", "amount": 600}
    data = sample_operations + [duplicate_date_operation]

    result = sort_by_date(data)
    # Должны сохраниться все операции, включая дубликат
    assert len(result) == 6
    # Операции с одинаковой датой должны быть рядом
    dec1_operations = [item for item in result if item.get("date") == "2023-12-01T12:00:00.000000"]
    assert len(dec1_operations) == 3


# Параметризованные тесты
@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 3),
        ("PENDING", 1),
        ("CANCELED", 1),
        ("UNKNOWN", 0),
    ],
)
def test_filter_by_state_parametrized(sample_operations, state, expected_count):
    """Тестируем filter_by_state с параметризацией"""
    result = filter_by_state(sample_operations, state)
    assert len(result) == expected_count


@pytest.mark.parametrize(
    "reverse, first_date",
    [
        (True, "2023-12-05T18:45:00.000000"),  # Новые сначала
        (False, "2023-10-10T04:20:00.000000"),  # Старые сначала
    ],
)
def test_sort_by_date_parametrized(sample_operations, reverse, first_date):
    """Тестируем sort_by_date с параметризацией"""
    result = sort_by_date(sample_operations, reverse)
    assert result[0]["date"] == first_date


if __name__ == "__main__":
    pytest.main(["-v", __file__])
