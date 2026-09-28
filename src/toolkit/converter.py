'''Конвертер величин: длина, масса, температура'''
from toolkit.errors import (
    AbsoluteZeroError,
    IncompatibleUnitsError,
    IncorrectValueError,
    UnknownUnitError,
)

lenght_units = ('mm', 'cm', 'm', 'km')
weight_units = ('g', 'kg')
temperature_units = ('c', 'f', 'k')

def transformation_float(digit:str) -> float:
    '''Превращает входное число в вещественное'''
    try:
        return float(digit)
    except ValueError: #переделываем ошибку в float в ошибку собственного errors
        raise IncorrectValueError('Неверное числовое значение')


def converter_lenght(initial_datas: float,initial_units: str, final_units: str) -> float:
    '''Функция перевода единиц измерения длины'''
    if initial_units == 'mm':
        si = initial_datas * 0.001
    elif initial_units == 'cm':
        si = initial_datas * 0.01
    elif initial_units == 'dm':
        si = initial_datas * 0.1
    elif initial_units == 'km':
        si = initial_datas * 1000.0
    else:
        si = initial_datas

    if final_units == 'mm':
        return si * 1000.0
    elif final_units == 'cm':
        return si * 100.0
    elif final_units == 'dm':
        return si * 10.0
    elif final_units == 'km':
        return si * 0.001
    else:
        return si


def converter_weight( initial_datas: float, initial_units: str, final_units: str) -> float:
    '''Функция перевода единиц измерения веса'''
    if initial_units == 'g':
        si = initial_datas * 0.001
    else:
        si = initial_datas

    if final_units == 'g':
        return si * 1000.0
    else:
        return si


def converter_temperature(initial_datas: float, initial_units: str, final_units: str) -> float:
    '''Функция перевода единиц измерения температуры'''
    if initial_units == 'c':
        si = initial_datas + 273.15
    elif initial_units == 'f':
        si = (initial_datas - 32) * (5/9) + 273.15
    else:
        si = initial_datas

    if si < -0.0000001:
        raise AbsoluteZeroError('Температура ниже абсолютного нуля')

    if final_units == 'c':
        return si - 273.15
    elif final_units == 'f':
        return (si - 273.15) * (9/5) + 32
    else:
        return si


def convert(initial_datas: float, initial_units: str, final_units: str) -> float:
    '''Определяет, какую функцию использовать, и выводит ошибки'''
    initial_datas = float(initial_datas)
    initial_units = initial_units.lower()
    final_units = final_units.lower()
    all_units = lenght_units + weight_units + temperature_units

    if initial_units not in all_units:
        raise UnknownUnitError('Неизвестная единица измерения')
    if final_units not in all_units:
        raise UnknownUnitError('Неизвестная единица измерения')

    if initial_units in lenght_units:
        if final_units not in lenght_units:
            raise IncompatibleUnitsError('Несовместимые единицы измерения')
        return converter_lenght(initial_datas, initial_units, final_units)

    if initial_units in weight_units:
        if final_units not in weight_units:
            raise IncompatibleUnitsError('Несовместимые единицы измерения')
        return converter_weight(initial_datas, initial_units, final_units)

    else:
        if final_units not in temperature_units:
            raise IncompatibleUnitsError('Несовместимые единицы измерения')
        return converter_temperature(initial_datas, initial_units, final_units)