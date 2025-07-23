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

    try:
        if full_data.lower().startswith("счет"):
            # Для счетов: "Счет <номер>"
            parts = full_data.split(maxsplit=1)
            return f"Счет {get_mask_account(parts[1])}" if len(parts) > 1 else "Счет **"
        else:
            # Для карт: "<Название> <номер>"
            *name_parts, number = full_data.rsplit(maxsplit=1)
            return f"{' '.join(name_parts)} {get_mask_card_number(number)}"
    except ValueError as e:
        return f"Ошибка: {str(e)}"


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
    print(mask_account_card("Visa Platinum 7000 7999 9999 6361"))  # Visa Platinum 7000 79** **** 6361
    print(mask_account_card("Счет 7365 4108 4301 3587 4305"))  # Счет **4305
    print(mask_account_card("МИР 1234 5678 9012 3456"))  # МИР 1234 56** **** 3456
    print(mask_account_card("Visa 1234567890123456"))  # Должно работать
    print(mask_account_card("Счет 12345678"))  # Должно работать
    # Тест даты
    print(get_date("2024-03-11T02:26:18.671407"))
    print(get_date("2021-12-31T23:59:59.999999"))
    print(get_date("2000-01-01T00:00:00.000000"))
