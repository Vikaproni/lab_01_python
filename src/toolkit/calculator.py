from decimal import ROUND_HALF_EVEN, Context, Decimal

from toolkit.errors import ZeroCalculatorError
from toolkit.tokeniz import tokenizator
from toolkit.validat import validation

context = Context(prec = 28, rounding = ROUND_HALF_EVEN) #политика округления: до 28 знаков после точки, округляет к ближайшему, а при равенстве к четной цифре


def unary_digit(tokens:list) -> list:
    '''Функция определяет унарные знаки и помечает их как отдельные операторы'''
    new_tokens = []
    position = 0
    expect_number = True
    while position < len(tokens):
        token = tokens[position]
        if token in '+-' and expect_number: #соединяет унарный знака с числом
            position += 1
            number = tokens[position]
            new_tokens.append('-' + number if token == '-' else number)
            expect_number = False
        else:
            new_tokens.append(token)
            if token in ('+','-','*','/','//','%','('): #определяем, что ждем - число или знак
                expect_number = True
            else:
                expect_number = False
        position += 1
    return new_tokens


def one_step_calculations(operator: str, left_operand: Decimal, right_operand: Decimal) -> Decimal:
    '''Подсчет одного действия выражения'''
    if operator == '+':
        return context.add(left_operand, right_operand) #сложение
    if operator == '-':
        return context.subtract(left_operand, right_operand) #вычитание
    if operator == '*':
        return context.multiply(left_operand, right_operand) #умножение

    if right_operand == 0: #проверка делителя на ноль
        raise ZeroCalculatorError('Деление на ноль')
    if operator == '/': #деление
        return context.divide(left_operand, right_operand)

    if operator == '//': #целочисленное деление
        return context.divide_int(left_operand, right_operand)
    if operator == '%': #остаток от деления
        return context.remainder(left_operand, right_operand)


priority = {'*':  2, '/': 2, '//': 2, '%': 2, '+': 1, '-': 1} #приоритет операций

def tokens_to_rpn(tokens: list[str]) -> list[str]:
    '''Перевод обычной записи выражения в польскую нотацию'''
    output = []
    stack = []
    for token in tokens:
        if token not in ('+','-','*','/','//','%','(',')'): #если токен не является оператором, сразу добавляем его в итоговый список
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')': #все, что накопилось - в output
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[token]: # если токен является оператором,
                # проверяется приоритет его операции, и если он больше,то токен сразу добавляется в стэк
                output.append(stack.pop())
            stack.append(token)
    while stack: #все в output
        output.append(stack.pop())
    return output


def calculate_in_rpn(tokens: list[str]) -> Decimal:
    '''Итоговый счет через перевод выражения в обратную польскую нотацию и вычисление стеком'''
    tokens = unary_digit(tokens)
    tokens_in_rpn = tokens_to_rpn(tokens)

    new_stack = []
    for token in tokens_in_rpn: #если токен число, добавляем его в стек
        if token not in ('+','-','*','/','//','%','(',')'):
            new_stack.append(Decimal(token))
        else: #если токен оператор, то забираем два последних числа из стека, считаем, и добавляем результат обратно в стек
            right_operand = new_stack.pop()
            left_operand = new_stack.pop()
            new_stack.append(one_step_calculations(token,left_operand,right_operand))
    return new_stack[0]


def finaly_result(expression: str) -> Decimal:
    tokens = tokenizator(expression)
    validation(tokens)
    return calculate_in_rpn(tokens)