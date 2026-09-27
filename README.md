# toolkit — калькулятор выражений и конвертер величин

Учебный пакет: арифметика без `eval` (токенизатор + обратная польская запись)
и конвертер длины/массы/температуры с CLI.

## Структура

- `src/toolkit/calculator.py` — ядро калькулятора (tokenize, validate, RPN)
- `src/toolkit/converter.py` — ядро конвертера (length, mass, temperature)
- `src/toolkit/errors.py` — иерархия ошибок (база `ToolkitError`)
- `src/toolkit/__main__.py` — CLI: подкоманды `calc` и `convert`
- `tests/` — юнит-тесты ядра и CLI

## Установка и запуск

    python3 -m toolkit calc "2+3*4"
    python3 -m toolkit convert 1000 --from mm --to m
    python3 -m toolkit --help

## Поддерживаемые единицы

- длина: mm, cm, m, dm, km
- масса: kg, g
- температура: c, k, f (регистр не важен)

## Коды возврата

- 0 — успех
- 2 — пользовательская ошибка (сообщение в stderr)

## Тесты и линтер

    python3 -m pytest -v
    ruff check .