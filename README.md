# Задача №4

## Принцип работы

Пишем в `Headers` следующие Key: Value

###

**Content-Type : application/json**

###

И передаем POST запрос с JSON данными на данный адресс `127.0.0.1:8000/api/json/`

###

Следующие данные:

```json
{
  "first_json": {
    "address": "2gis.url.com",
    "timeout": 50,
    "proxy-server": "3.102.198.51",
    "deny": true
  },
  "second_json": {
    "timeout": 1050,
    "proxy-server": "3.102.198.51",
    "verbose": true
  }
}

```

Ответ будет слудеющим

```json
{
  "first_json": {
    "address": "2gis.url.com",
    "timeout": 50,
    "proxy-server": "3.102.198.51",
    "deny": true
  },
  "second_json": {
    "timeout": 1050,
    "proxy-server": "3.102.198.51",
    "verbose": true
  },
  "result": {
    "D": {
      "timeout": {
        "N": 1050,
        "O": 50
      },
      "deny": {
        "R": true
      },
      "address": {
        "R": "2gis.url.com"
      },
      "proxy-server": {
        "U": "3.102.198.51"
      },
      "verbose": {
        "A": true
      }
    }
  }
}
```

Сервер принимает два JSON файла и дальше идёт обработка этих JSON и после чего происходит ответ с сервера 
