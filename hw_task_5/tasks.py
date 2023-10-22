import pandas as pd
import numpy as np
from string import ascii_lowercase
import matplotlib.pyplot as plt


def task1():
    return pd.DataFrame(np.random.randint(1, 11, size=(10, 10)))


def task2():
    frame = task1()
    frame.index = list(ascii_lowercase[:10])
    frame_res = frame.loc[lambda x: x.min(axis=1) > 5]
    if not frame_res.empty:
        print(frame_res.iloc[0])


def task3():
    frame = pd.DataFrame(np.random.randint(1, 11, size=(10, 10)),
                         index=list(ascii_lowercase[:10]), columns=list(ascii_lowercase[:10]))
    print(frame.shape)
    print(frame.index)
    print(frame.mean().mean())
    frame.to_csv('task3.csv')


def task4():
    frame = pd.read_csv('emojis.csv')
    popularity = frame.groupby('Category')['Rank'].mean().sort_values()
    print(popularity.index[0])


def task5():
    frame = pd.read_csv('emojis.csv')
    by_year = frame['Year'].value_counts().sort_index()
    by_year.plot()
    plt.show()


def task6(category_name: str):
    frame = pd.read_csv('emojis.csv')
    n = len(frame)
    by_cat = frame['Category'].value_counts()
    if category_name in by_cat.index:
        return 100 * by_cat[category_name] / n
    return "This category doesn't exist"


def task7(first_date: str, second_date: str):
    first_date = pd.to_datetime(first_date)
    second_date = pd.to_datetime(second_date)
    frame = pd.read_csv('BCT-USD.csv')
    frame['Date'] = pd.to_datetime(frame['Date'])
    period = frame[frame['Date'] > first_date]
    period = period[period['Date'] < second_date]
    period = period.set_index('Date')
    period['Open'].plot()
    period['Close'].plot()
    plt.show()


def task8():
    frame = pd.read_csv('BCT-USD.csv')
    frame['Date'] = pd.to_datetime(frame['Date'])
    print(frame.sort_values('Volume').iloc[0]['Date'].month_name())


def task9():
    frame = pd.read_csv('BCT-USD.csv')
    frame['Date'] = pd.to_datetime(frame['Date'])
    combined = frame.loc[[item['Date'].is_month_start or item['Date'].is_month_end for _, item in frame.iterrows()]]
    result = []
    start_open = None
    for _, row in combined.iterrows():
        if row['Date'].is_month_end:
            if start_open is None:
                continue
            end_close = row['Close']
            if end_close > start_open:
                result.append(row['Date'].month_name() + ' ' + str(row['Date'].year))
            start_open = None
        else:
            start_open = row['Open']
    if result:
        return result
    print('No months found')
