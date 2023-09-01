from time import perf_counter
from random import choice


def task1(in_str: str) -> str:
    stop = ['Python', 'php', 'go', 'C']
    words = in_str.split()
    res = filter(lambda x: x not in stop, words)
    return ' '.join(res)


def task2(number, tested_list: list) -> list:
    return list(filter(lambda x: x % number == 0, tested_list))


def task3(*args) -> tuple:
    return tuple(filter(lambda x: type(x) == str, args))


def task4(list1: list, list2: list) -> list:
    return list(filter(lambda x: x in list2, list1))


def task5(n: int) -> int:
    if n == 1:
        return 1
    res = 1 if n % 2 != 0 else 0
    max_on_top = int(n / 2)
    for amount_on_top in range(1, max_on_top + 1):
        res += task5(amount_on_top)
    return res


def task6_decorator(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        if type(res) != int:
            raise TypeError(f'Function must return int type, got {type(res)} instead')
        return res
    return wrapper


@task6_decorator
def task6_func1():
    return choice((1, '1', 5, False, (1, 2, 3), 89))


@task6_decorator
def task6_func2(k):
    return k


def task7_decorator(fn):
    def wrapper(*args, **kwargs):
        try:
            res = fn(*args, **kwargs)
        except Exception:
            print('Error occurred, restarting function')
            res = fn(*args, **kwargs)
        return res
    return wrapper


@task7_decorator
def task7_func1():
    k = choice((0, 2))
    return 16 / k


@task7_decorator
def task7_func2():
    n = choice((1, '1'))
    return 8 + n


def task8(elements: list = None) -> list:
    if elements is None:
        elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
    result = sorted(elements, key=lambda item: item[1])
    return result


def task9_decorator(fn):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        res = fn(*args, **kwargs)
        stop = perf_counter()
        print(f'Function {fn.__name__} executed in {stop - start} seconds')
        return res
    return wrapper


@task9_decorator
def task9_func1():
    res = 0
    for i in range(500_000_000):
        res += i
    return res


@task9_decorator
def task9_func2():
    return sum(range(500_000_000))

