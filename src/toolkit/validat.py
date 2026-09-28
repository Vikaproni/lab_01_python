'''Функция валидации. Проверяет корректность введенного выражения.'''
from toolkit.errors import (
    DoubleCalculatorError,
    EmptyCalculatorError,
    MissingOperandError,
    MissingOperatorError,
    NotDepthError,
)


def validation(tokens: list[str]) -> None:
    if not tokens:
        raise EmptyCalculatorError('Пустое выражение')

    operators = ['+', '-', '*', '/', '//', '%']
    need_operand = True
    last_operator = False
    after_unary_operator = False # флаг для унарного оператора
    count_depth = 0 #счетчик скобок

    for token in tokens:
        if token == '(':
            if not need_operand:
                raise MissingOperatorError('Нет оператора перед "("')
            if after_unary_operator: #установление ошибки унарного знака перед скобкой
                raise MissingOperatorError('Отсутствие оператора')
            count_depth += 1
            last_operator = False
            after_unary_operator = False

        elif token == ')':
            if need_operand:
                raise MissingOperandError('Нет числа перед ")" или пустые скобки')
            if count_depth == 0:
                raise NotDepthError('Не хватает скобки')
            count_depth -= 1

        elif token in operators:
            if need_operand:
                if token in ('+','-'):
                    if after_unary_operator:
                        raise DoubleCalculatorError('Ошибка унарных операторов')
                    last_operator = True
                    after_unary_operator = True
                    continue
                if last_operator: #если до этого уже был оператор
                    raise DoubleCalculatorError('Лишние операторы')
                raise MissingOperandError('Отсутствие операнда')
            need_operand = True
            last_operator = True
            after_unary_operator = False

        else:
            if not need_operand:
                raise MissingOperatorError('Отсутствует оператор между числами')
            last_operator = False
            need_operand = False
            after_unary_operator = False


    if need_operand:
        raise MissingOperandError('Отсутствие операнда в конце выражение')
    if count_depth != 0: #ловим ошибку незакрытых скобок
        raise NotDepthError('Не хватает скобок')