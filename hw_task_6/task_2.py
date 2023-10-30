import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from os import path
from time import perf_counter


class Network:
    def __init__(self, epochs: int, batch: int, *args):
        """
        Класс нейронной сети

        :param epochs: Количество эпох
        :param batch: Расмер батча
        :param args: Количество нейронов в слоях (количество слоев произвольное)
        """
        self.epochs = epochs
        self.batch = batch
        self.model = Sequential()
        self.neurons_num = args
        for index, value in enumerate(args):
            if index == 0:
                self.model.add(Dense(value, input_dim=8, activation='relu'))
            else:
                self.model.add(Dense(value, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    @classmethod
    def prepare_data(cls, file_path, test_amount=20):
        """
        Метод подготовки данных

        :param file_path: Путь к файлу с данными
        :param test_amount: Количество строк данных, применяемых для тестирования
        """
        data = np.genfromtxt('data.txt', delimiter=',')
        input_data = data[:, :-1]
        results = data[:, -1].astype(int)

        cls.training_input = input_data[test_amount:, :]
        cls.training_results = results[test_amount:]

        cls.test_input = input_data[:test_amount, :]
        cls.test_results = results[:test_amount]

    def learning(self):
        self.model.fit(self.training_input, self.training_results, epochs=self.epochs, batch_size=self.batch, verbose=2)

    def inference(self, print_to_file=False, folder_name=path.curdir):
        prediction = self.model.predict(self.test_input)
        prediction_rounded = np.rint(prediction).flatten().astype(int)
        comparison = prediction_rounded == self.test_results
        percentage = 100 * np.bincount(comparison)[1] / len(comparison)
        print('Доля верных предсказаний: ', str(percentage) + '%')
        if print_to_file:
            with open(path.join(folder_name,
                                f'inference_neurons_{self.neurons_num}_epochs_{self.epochs}_batch_{self.batch}.txt'),
                      'a') as file:
                file.write(f'neurons: {self.neurons_num} epochs {self.epochs} batch {self.batch}\n')
                file.write(f'prediction: {prediction_rounded}\n')
                file.write(f'correct results: {self.test_results}\n')
                file.write(f'accuracy: {percentage}\n')

        return prediction_rounded


if __name__ == '__main__':
    stt = perf_counter()
    Network.prepare_data('data.txt', 10)
    n = Network(10, 10, 120, 80, 33, 15)
    n.learning()
    n.inference()
    stp = perf_counter()
    print('Время работы, c:')
    print(stp - stt)
