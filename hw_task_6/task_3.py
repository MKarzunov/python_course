from task_2 import Network
from os import mkdir, path, system
from shutil import rmtree


if not path.isdir('cycle_results'):
    mkdir('cycle_results')
else:
    rmtree('cycle_results')
    mkdir('cycle_results')

Network.prepare_data('data.txt', 15)

for first_num in range(5, 16):
    for second_num in range(4, 11):
        for epochs in range(10, 51, 5):
            for batch in range(10, 51, 5):
                web = Network(epochs, batch, first_num, second_num)
                for _ in range(3):
                    web.learning()
                    web.inference(True, 'cycle_results')


system("shutdown /s /t 1")
