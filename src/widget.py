def mask_account_card_widget(full_data: str) -> str:
    """
    Маскирует номер карты/счета для виджета.
    Аргумент:
        full_data (str): "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"
    Возвращает:
        str: "Visa Platinum 7000 79** **** 6361" или "Счет **4305"
    """
    if not full_data:
        raise ValueError("Пустая строка")

    parts = full_data.split()

    if len(parts) < 2:
        raise ValueError("Неверный формат. Пример: 'Visa Platinum 7000792289606361'")

    if "Счет" in full_data:
        account_number = "".join([c for c in parts[-1] if c.isdigit()])  # Оставляем только цифры
        if len(account_number) < 4:
            raise ValueError("Номер счета должен содержать минимум 4 цифры")
        return f"Счет **{account_number[-4:]}"
    else:
        card_number = "".join([c for c in parts[-1] if c.isdigit()])
        if len(card_number) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр")
        return f"{' '.join(parts[:-1])} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


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
