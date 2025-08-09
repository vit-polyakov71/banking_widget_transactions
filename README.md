
# Проект "Банковские транзакции"

Проект разработан в рамках обучения для реализации бэкенд-логики виджета банковских операций.

## Реализованные функции

### 1. Обработка операций (`processing.py`)
- `filter_by_state()` - фильтрует операции по статусу ("EXECUTED"/"CANCELED")
- `sort_by_date()` - сортирует операции по дате (новые→старые или наоборот)

### 2. Маскировка данных (`masks.py`)
- `get_mask_card_number()` - маскирует номер карты (вид: 7000 79** **** 6361)
- `get_mask_account()` - маскирует номер счета (вид: **4305)

### 3. Универсальный виджет (`widget.py`)
- `mask_account_card()` - автоматически определяет тип данных (карта/счет) и применяет соответствующую маскировку

## Как использовать

1. Склонируйте репозиторий:
```bash
git clone https://github.com/vit-polyakov71/banking_widget_transactions.git
cd banking_widget_transactions

2. Импортируйте нужные функции:
from src.processing import filter_by_state, sort_by_date
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card

3. Примеры использования:
# Фильтрация операций
operations = [
    {"state": "EXECUTED", "date": "2023-01-01"},
    {"state": "CANCELED", "date": "2023-01-02"}
]
filtered = filter_by_state(operations)

# Маскировка данных
card_mask = get_mask_card_number("7000792289606361")  # 7000 79** **** 6361
account_mask = get_mask_account("73654108430135874305")  # **4305

# Универсальная маскировка
widget_mask1 = mask_account_card("Visa Platinum 7000792289606361")  # Visa Platinum 7000 79** **** 6361
widget_mask2 = mask_account_card("Счет 73654108430135874305")  # Счет **4305

# Структура проекта:
banking_widget_transactions/
├── src/
│   ├── processing.py  # Фильтрация и сортировка
│   ├── masks.py       # Маскировка данных
│   └── widget.py      # Универсальный обработчик
├── tests/             # Тесты
└── README.md          # Этот файл


Примечание
Проект находится в активной разработке. Дополнительные функции и документация будут добавляться по мере реализации.
