from masks import get_mask_card_number, get_mask_account


def mask_account_card(full_data: str) -> str:
    """
    Маскирует номер карты или счета, используя функции из модуля masks.

    Args:
        full_data: Строка формата "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"

    Returns:
        Строка с замаскированным номером (для карт: "7000 79** **** 6361", для счетов: "**4305")

    Raises:
        ValueError: Если входные данные некорректны
    """
    if not full_data.strip():
        raise ValueError("Получена пустая строка")

    normalized = ' '.join(full_data.strip().split())

    if normalized.lower().startswith("счет"):
        parts = normalized.split(maxsplit=1)
        if len(parts) < 2:
            raise ValueError("Неверный формат счета")
        account_num = parts[1].replace(" ", "")
        return f"Счет {get_mask_account(account_num)}"
    else:
        # Обработка карты - находим номер карты (последние 16+ цифр)
        # Разделяем строку на слова
        words = normalized.split()

        # Находим номер карты (последний элемент, содержащий цифры)
        number_part = words[-1]
        number = number_part.replace(" ", "")

        if len(number) != 16:
            # Собираем все цифры из строки
            all_digits = ''.join(c for c in normalized if c.isdigit())
            if len(all_digits) >= 16:
                number = all_digits[-16:]  # Берем последние 16 цифр
            else:
                raise ValueError(f"Номер карты должен содержать 16 цифр (получено {len(all_digits)})")

            # Название карты - все до номера
        name = normalized[:-len(number)].strip()

        return f"{name} {get_mask_card_number(number)}"


def get_date(datetime_str: str) -> str:
    """
    Конвертирует дату из формата ISO в 'ДД.ММ.ГГГГ'.

    Аргументы:
        datetime_str: строка с датой и временем (например, '2024-03-11T02:26:18.671407')

    Возвращает:
        Строку с датой в формате 'ДД.ММ.ГГГГ' (например, '11.03.2024')

    Пример:
        >>> get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'
    """

    if not datetime_str:
        raise ValueError("Пустая строка с датой")

    if "T" not in datetime_str:
        raise ValueError("Некорректный формат. Ожидается 'YYYY-MM-DDTHH:MM:SS'")

    date_part = datetime_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"


if __name__ == "__main__":
    # Тестовые примеры
    print(mask_account_card("Visa Platinum 7000792289606361"))  # Без пробелов
    print(mask_account_card("Счет 73654108430135874305"))  # Счет
    print(mask_account_card("МИР 1234 5678 9012 3456"))  # С пробелами
    print(mask_account_card("Visa Classic 1234 5678 9012 3456"))  # С пробелами
    # Тест даты
    print(get_date("2024-03-11T02:26:18.671407"))
    print(get_date("2021-12-31T23:59:59.999999"))
    print(get_date("2000-01-01T00:00:00.000000"))
