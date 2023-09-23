import numpy as np
import re


def task_1():
    print(np.sort(np.random.randint(100, size=10)))


def task_2():
    return np.array([[0, 1] * 4, [1, 0] * 4] * 4)


def task_3():
    m1 = np.random.randint(10, size=(8, 4))
    m2 = np.random.randint(10, size=(4, 2))
    print(np.dot(m1, m2))


def task_4():
    step = 1 / 11
    return np.arange(step, 1, step)


def task_5(number: int):
    not_found = True
    for i in range(2, number):
        if number % i == 0:
            not_found = False
            print(np.ones((i, int(number / i))), end='\n\n')
    if not_found:
        print('No matrixes can be created')


class Task6:
    def __init__(self, path):
        self.path = path
        self.content = None

    def read(self):
        with open(self.path, 'r') as file:
            self.content = file.read().split('\n')

    def find_match(self, pattern):
        res = []
        for line in self.content:
            res.extend(re.findall(pattern, line))
        return res


def task_7(a: np.array, s: int, last: bool = False):
    b = np.random.randint(100, size=(s, len(a)))
    to_sum = np.dot(b, a)
    x = np.sum(to_sum, axis=0)
    pass


task_7(np.array((1, 2, 3, 4, 5)), 10)
