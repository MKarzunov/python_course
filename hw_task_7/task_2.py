from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

np.set_printoptions(precision=2, floatmode='fixed', suppress=True)
passengers = pd.read_csv('titanic.csv',
                         converters={'PClass': lambda classnum: int(classnum[0])})
passengers = passengers[passengers['Age'].notna()]

results = np.array(passengers['Survived'], dtype=int)
inputs = np.array(passengers[['PClass', 'Age', 'SexCode']], dtype=int)

X_train = inputs[10:, :]
Y_train = results[10:]

X_test = inputs[:10, :]
Y_test = results[:10]

model = svm.SVC()
model.fit(X_train, Y_train)

predicted = model.predict(X_test)
correct = predicted == Y_test
correct_share = np.bincount(correct)[1] / len(correct)
print(f'Предсказания\n{predicted}')
print(f'Ответы\n{Y_test}')
print(f'Верных ответов {correct_share * 100}%')
