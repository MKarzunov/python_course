import numpy as np
from keras.models import Sequential
from keras.layers import Dense

data = np.genfromtxt('data.txt', delimiter=',')
input_data = data[:, :-1]
results = data[:, -1].astype(int)

test_amount = 3

training_input = input_data[test_amount:, :]
training_results = results[test_amount:]

test_input = input_data[:test_amount, :]
test_results = results[:test_amount]

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(training_input, training_results, epochs=15, batch_size=10, verbose=2)

prediction = model.predict(test_input)
prediction_rounded = np.rint(prediction).flatten()

comparison = prediction_rounded == test_results
percentage = 100 * np.bincount(comparison)[1] / len(comparison)
print('Доля верных предсказаний: ', str(percentage) + '%')
pass
