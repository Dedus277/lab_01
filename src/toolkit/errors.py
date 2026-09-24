class ToolkitError(Exception):
    """Базовый класс для всех ошибок пакета toolkit."""
    pass

# --- Ошибки калькулятора ---

class EmptyExpressionError(ToolkitError):
    """Выражение пустое или состоит только из пробелов."""
    pass

class InvalidCharacterError(ToolkitError):
    """В выражении обнаружен недопустимый символ."""
    pass

class MissingOperandError(ToolkitError):
    """Пропущен операнд (например, '2 + ' или '+ 2' в начале без унарности)."""
    pass

class ConsecutiveOperatorsError(ToolkitError):
    """Два бинарных оператора подряд (например, '2 + * 3')."""
    pass

class DivisionByZeroError(ToolkitError):
    """Попытка деления на ноль."""
    pass

class InvalidNumberError(ToolkitError):
    """Неверное числовое значение (например, '2.5.6')."""
    pass

# --- Ошибки конвертера ---

class UnknownUnitError(ToolkitError):
    """Указана неизвестная единица измерения."""
    pass

class IncompatibleUnitsError(ToolkitError):
    """Попытка конвертировать несовместимые единицы (например, кг в метры)."""
    pass

class BelowAbsoluteZeroError(ToolkitError):
    """Температура ниже абсолютного нуля."""
    pass