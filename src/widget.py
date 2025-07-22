


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
    # Тесты карт и счетов
    print(mask_account_card_widget("Счет 73654108430135874305"))  # "Счет **4305"
    print(mask_account_card_widget("Visa Platinum 7000792289606361"))  # "Visa Platinum 7000 79** **** 6361"
    print(mask_account_card_widget("Maestro 1596837868705199"))
    print(mask_account_card_widget("Счет 64686473678894779589"))
    print(mask_account_card_widget("Счет 123"))
    # Тест даты
    print(get_date("2024-03-11T02:26:18.671407"))
    print(get_date("2021-12-31T23:59:59.999999"))
    print(get_date("2000-01-01T00:00:00.000000"))
