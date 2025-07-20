def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты в формате XXXX XX** **** XXXX
    Args:
        card_number: Номер карты (16 цифр) в виде строки
    Returns:
        Маскированная строка
    Raises:
        ValueError: Если номер не содержит 16 цифр
    """
    card_number = card_number.replace(" ", "")  # Удаляем пробелы
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    if not card_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")
    part_1 = card_number[:4]
    part_2 = card_number[4:6]
    part_4 = card_number[-4:]
    return f"{part_1} {part_2}** **** {part_4}"


def get_mask_account(account_number: str | int) -> str:
    """
    Маскирует номер счёта в формате **XXXX
    Args:
        account_number: Номер счёта в виде строки
    Returns:
        Маскированная строка (последние 4 цифры с ** в начале)
    Raises:
        ValueError: Если номер слишком короткий или содержит нецифровые символы
    """
    cleaned_number = str(account_number).replace(" ", "")
    if not cleaned_number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")
    if len(cleaned_number) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    return f"**{cleaned_number[-4:]}"


if __name__ == "__main__":
    # Тесты для карт
    print(get_mask_card_number("7000792289606361"))  # Должно вернуть "7000 79** **** 6361"
    print(get_mask_card_number("7000 7922 8960 6361"))  # Также работает (удаляет пробелы)

    # Тесты для счетов
    print(get_mask_account("73654108430135874305"))  # "**4305"
    print(get_mask_account("1234"))  # "**1234"
    print(get_mask_account(12345678))  # Работает с числами: "**5678"
