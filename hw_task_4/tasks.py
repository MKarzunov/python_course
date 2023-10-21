import numpy as np
import re
import pandas as pd


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
        print('No matriсes can be created')


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


def my_to_datetime(inp: str):
    if '24:00' in inp:
        return inp.replace('24:00', '23:59')
    return inp


class Task8:
    path = 'nlo.csv'

    def __init__(self):
        self.info = None

    def read_file(self):
        self.info = pd.read_csv(self.path, on_bad_lines='skip')
        # self.info['datetime'] = pd.to_datetime(self.info['datetime'], errors='raise', format='%#m/%#d/%Y %H:%M')
        self.info['datetime'] = self.info['datetime'].apply(my_to_datetime)
        self.info['datetime'] = pd.to_datetime(self.info['datetime'])
        pass

    def get_most_frequent_country(self):
        return self.info['state'].value_counts().index[0]

    def get_most_frequent_month(self):
        k = self.info['datetime'].apply(pd.Timestamp.month_name)
        return k.value_counts().index[0]


def integer_translator(inp: str):
    try:
        return int(inp)
    except ValueError:
        return 0


def separator(inp: str):
    while ' /' in inp:
        inp = inp.replace(' /', '/')
    while '/ ' in inp:
        inp = inp.replace('/ ', '/')
    inp = inp.strip('/')
    return inp.split('/')


class Task9:
    path = 'all_ai_tool.csv'

    def __init__(self):
        self.info = None

    def read_file(self):
        self.info = pd.read_csv(self.path, converters={'Review': integer_translator, 'Useable For': separator})
        self.info['Free/Paid/Other'] = self.info['Free/Paid/Other'].apply(lambda x: 'Free' if x == 'Free' else 'Paid')
        pass

    def most_reviewable_type(self):
        k = self.info.groupby('Free/Paid/Other')['Review'].sum().sort_values(ascending=False)
        return k.index[0]

    def most_common_free_usage(self):
        free = self.info[self.info['Free/Paid/Other'] == 'Free']
        res = free.explode('Useable For').groupby('Useable For')['Useable For'].count().sort_values(ascending=False)
        return res.index[0]

    def get_best_tools(self, monetization: str = '', usage: str = '', category: str = ''):
        by_mon = self.info[self.info['Free/Paid/Other'] == monetization] if monetization else self.info
        by_cat = by_mon[by_mon['Major Category'] == category] if category else by_mon
        exploded = by_cat.explode('Useable For')
        by_usage = exploded[exploded['Useable For'] == usage] if usage else by_cat
        best = by_usage.sort_values('Review', axis=0, ascending=False)
        return best.head(3)['AI Tool Name'].to_list()
