"""Ошибки пакета toolkit"""

class ToolkitError(Exception):
    '''Базовая ошибка пакета'''

class ConverterError(ToolkitError):
    '''Ошибка при конвертировании'''

class UnknownUnitError(ConverterError):
    '''Неизвестная единица'''

class IncompatibleUnitsError(ConverterError):
    '''Несовместимые единицы'''

class AbsoluteZeroError(ConverterError):
    '''Ниже абсолютного нуля'''

class IncorrectValueError(ConverterError):
    '''Неверное числовое значение '''

class CalculatorError(ToolkitError):
    '''Ошибка при вычислении'''

class EmptyCalculatorError(CalculatorError):
    '''Пустое выражение'''

class InvalidCalculatorError(CalculatorError):
    """Недопустимый символ"""

class MissingOperandError(CalculatorError):
    """Пропущенный операнд"""

class DoubleCalculatorError(CalculatorError):
    """Два бинарных оператора подряд"""

class ZeroCalculatorError(CalculatorError):
    """Деление на ноль"""

class MissingOperatorError(CalculatorError):
    """Отсутствие оператора"""

class NotDepthError(CalculatorError):
    """Не хватает скобки"""


