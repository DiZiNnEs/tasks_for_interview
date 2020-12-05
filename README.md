# Задача №3

## Принцип работы

Пишем в `Headers` следующие Key: Value
###
**Content-Type : application/json**
###
И передаем POST запрос с JSON данными на данный адресс `127.0.0.1:8000/api/multiply/`
###
Следующие данные:
```json
{
    "multipliers": [1, 2, 3, 4]
}Л
```
_~~Будет происходить~~ `1 * 2 * 3 * 4 = 24`_
###
Ответ будет слудеющим
```json
{
    "Введенные данные": [
        1,
        2,
        3,
        4
    ],
    "Результат": 24
}
```

## Тесты
Тесты прописаны в файле `tests.py`
