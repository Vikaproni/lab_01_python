'''Функция токенизации выражения. Получает на вход строку с выраженем и преобразует ее в список токенов, разбивая выражения на числа и операторы.'''
from toolkit.errors import (
    InvalidCalculatorError,
)

numbers = '0123456789.'
operators = '-+*/%()'

def tokenizator(expression: str)-> list[str]:
    tokens = [] #создание списка для будущих токенов
    position = 0
    while position < len(expression):
        char = expression[position] #задаем проверяемый символ
        if char.isspace(): #проверка, не является ли символ пробелом
            position += 1
            continue
        if expression[position:position+2] == '//': #проверка на оператор целочисленного деления
            tokens.append(expression[position:position+2])
            position += 2
            continue
        if char in operators: #проверка, не является ли символ оператором
            tokens.append(char)
            position += 1
            continue
        if char in numbers: #проверка, не является ли символ числом (целым или вещественным)
            end = position
            dots = 0
            while end < len(expression) and (expression[end] in numbers):
                if expression[end] == '.': #считывание вещественного числа
                    dots += 1
                    if dots > 1:
                        raise InvalidCalculatorError('Недопустимый символ')
                end += 1
            digit = expression[position:end]
            if digit == '.':
                raise InvalidCalculatorError('Недопустимый символ')
            tokens.append(expression[position:end])
            position = end
            continue
        raise InvalidCalculatorError('Недопустимый символ') #вывод ошибки недопустимого символа
    return tokens #возвращает токинизированный список элементов