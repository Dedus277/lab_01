class ToolkitError(Exception):
    """Базовый класс для всех ошибок пакета toolkit."""

# --- Ошибки калькулятора ---

class EmptyExpressionError(ToolkitError):
    """Выражение пустое или состоит только из пробелов."""

class InvalidCharacterError(ToolkitError):
    """В выражении обнаружен недопустимый символ."""

class MissingOperandError(ToolkitError):
    """Пропущен операнд (например, '2 + ' или '+ 2' в начале без унарности)."""

class ConsecutiveOperatorsError(ToolkitError):
    """Два бинарных оператора подряд (например, '2 + * 3')."""

class DivisionByZeroError(ToolkitError):
    """Попытка деления на ноль."""

class InvalidNumberError(ToolkitError):
    """Неверное числовое значение (например, '2.5.6')."""

# --- Ошибки конвертера ---

class UnknownUnitError(ToolkitError):
    """Указана неизвестная единица измерения."""

class IncompatibleUnitsError(ToolkitError):
    """Попытка конвертировать несовместимые единицы (например, кг в метры)."""

class BelowAbsoluteZeroError(ToolkitError):
    """Температура ниже абсолютного нуля."""
