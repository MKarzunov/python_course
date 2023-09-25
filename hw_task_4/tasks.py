import numpy as np
import re
import pandas as pd
import datetime as dt


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
    b = np.random.random((s, len(a)))
    to_sum = a * b
    x = np.sum(to_sum, axis=1)
    res = np.maximum(x, 0) if last else np.sin(x)
    return res, b


r1, _ = task_7(np.random.random(5), 10)
r2, _ = task_7(r1, 10)
r3, _ = task_7(r2, 5, True)
print(r3 * 100)


def my_to_datetime(inp: pd.Series):
    for item in inp:
        if item[11:13] != '24':
            item = pd.to_datetime(inp, format='%#m/%#d/%Y %H:%M')

        time_fixed = item[0:11] + '00' + inp[13:]
        item = pd.to_datetime(time_fixed, format='%m/%d/%Y %H:%M') + dt.timedelta(days=1)
    return inp


class Task8:
    path = 'nlo.csv'

    def read_file(self):
        self.info = pd.read_csv(self.path, on_bad_lines='skip')
        # self.info['datetime'] = pd.to_datetime(self.info['datetime'], errors='raise', format='%#m/%#d/%Y %H:%M')
        self.info['datetime'] = my_to_datetime(self.info['datetime'])
        pass

    def get_most_frequent_country(self):
        return self.info['state'].value_counts().index[0]

    def get_most_frequent_month(self):
        return self.info['state'].value_counts().index[0]


t = Task8()
t.read_file()
print(t.get_most_frequent_country())

m = dt.datetime.now()
print(m.strftime('%#m/%#d/%Y %H:%M'))
