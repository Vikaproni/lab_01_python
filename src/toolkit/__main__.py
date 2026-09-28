import argparse
import sys
from decimal import Decimal

from toolkit.calculator import finaly_result
from toolkit.converter import convert, transformation_float
from toolkit.errors import ToolkitError


def beautiful_number(number:float| Decimal) -> str:
    '''Убирает ненужные нули у целых чисел.'''
    if isinstance(number, Decimal): #приведение числа к обычному виду, не экспоненциальному
        answer = format(number,'f')
    else:
        answer = str(number)

    if '.' in answer: #убираем ненужные нули в дробной части числа
        answer = answer.rstrip('0')
        answer = answer.rstrip('.')

    if answer in ('','-','-0'): #проверка крайних случаев
        answer = '0'

    return answer


def no_flag(expression: list[str]) -> list[str]:
    '''Проверяет не является ли выражение флагом.'''
    if len(expression) >= 2 and expression[0] == 'calc' and expression[1] not in ('--', '-h', '--help'): #вставляем "--", чтобы выражение считалось правильно
        return [expression[0], '--', expression[1]] + expression[2:]
    return expression


def main(expression: list[str]| None = None) -> None:
    arm_arguments: list[str] = list(sys.argv[1:]) if expression is None else list(expression) #если аргументы
    # переданы через терминал, берем их из sys.argv, иначе просто используем их

    parser = argparse.ArgumentParser(prog='toolkit', description='Калькулятор и конвертер')
    subparsers = parser.add_subparsers(dest='command', required=True, help='доступные команды') #создание подкоманд

    calc_parser = subparsers.add_parser('calc', help='вычислить арифметическое выражение')
    calc_parser.add_argument('expression', help='арифметическое выражение выражение')

    convert_parser = subparsers.add_parser('convert', help='перевод единиц измерения')
    convert_parser.add_argument('initial_datas', help='числовое значение')
    convert_parser.add_argument('--from', dest='initial_units', required=True, help='начальная единица измерения')
    convert_parser.add_argument('--to', dest='final_units', required=True, help='конечная единица измерения')

    arguments = parser.parse_args(no_flag(arm_arguments))

    try: #определяет для какой команды какой результат
        if arguments.command == 'calc':
            result = finaly_result(arguments.expression)
        else:
            initial_datas = transformation_float(arguments.initial_datas)
            result = convert(initial_datas, arguments.initial_units, arguments.final_units)
    except ToolkitError as error:
        print('Ошибка: ' + str(error), file=sys.stderr)
        sys.exit(2)

    print(beautiful_number(result))


if __name__ == '__main__':
    main()
