def task_1(s: str = '') -> int:
    return len(s)


def task_2(l1: list, l2: list) -> int:
    return max(len(l1), len(l2))


def task_3(inp_list: list, addition) -> list:
    inp_list.append(addition)
    return inp_list


def task_4(number):
    print('+' if -100 <= number <= 100 else '-')


def task_5(str_1: str, str_2: str) -> str:
    return 'ДА' if str_1 in str_2 else 'НЕТ'


def task_6(inp_list: list) -> int:
    if len(inp_list) != 5:
        raise ValueError(f'List length must be 5, got {len(inp_list)} instead')
    return len([item for item in inp_list if item > 0])


def task_7(years: int, months: int):
    print(years * 365 + months * 29)


def task_8(inp: str):
    if type(inp) != str:
        raise TypeError(f'Input value must be of str type, got {type(inp)} instead')
    print(''.join([item[0].capitalize() for item in inp.split()]))


def task_9(number: int) -> int:
    return 1 if number == 0 else task_9(number - 1) * number


def task_10(in_list: list) -> list:
    return list(map(lambda pair: pair[0] * pair[1], enumerate(in_list)))
