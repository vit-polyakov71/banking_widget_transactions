def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей по значению ключа 'state'."""
    result_list = []
    for item in data:
        if item.get("state") == state:
            result_list.append(item)
    return result_list


# Пример данных для проверки (добавьте в конец файла)
test_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Вызов функции и вывод результата
if __name__ == "__main__":
    print("Фильтр по EXECUTED:")
    print(filter_by_state(test_data))  # Проверка значения по умолчанию

