from datetime import datetime
from typing import Dict, Any, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список словарей по значению ключа 'state'."""
    result_list: List[Dict[str, Any]] = []
    for item in data:
        if item.get("state") == state:
            result_list.append(item)
    return result_list


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по полю 'date'.

    Args:
        data: Список словарей для сортировки.
        reverse: Если True (по умолчанию), сортировка по убыванию (новые сначала).
                 Если False, сортировка по возрастанию (старые сначала).

    Returns:
        Новый список словарей, отсортированный по полю 'date'.
    """
    if not data:
        return []

    def get_date(item: Dict[str, Any]) -> datetime:
        date_str = item.get("date")
        if not date_str:
            return datetime.min  # Если даты нет, помещаем в начало/конец
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")

    return sorted(data, key=get_date, reverse=reverse)


# Пример данных для проверки
test_data_filter: List[Dict[str, Any]] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

test_data_sort: List[Dict[str, Any]] = [
    {"id": 1, "date": "2023-01-01T12:00:00.000000"},
    {"id": 2, "date": "2023-01-02T12:00:00.000000"},
    {"id": 3},  # Элемент без даты
]


if __name__ == "__main__":
    print("=== Тест фильтрации ===")
    print("Фильтр по EXECUTED:")
    print(filter_by_state(test_data_filter))

    print("\n=== Тест сортировки ===")
    print("Сортировка по убыванию (новые сначала):")
    print(sort_by_date(test_data_sort))

    print("\nСортировка по возрастанию (старые сначала):")
    print(sort_by_date(test_data_sort, reverse=False))
