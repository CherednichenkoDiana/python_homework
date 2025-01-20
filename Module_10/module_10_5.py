import threading
import multiprocessing
from multiprocessing import Pool
import time

def read_info(name):
    all_data =[]
    with open(name, encoding='utf-8') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break

if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
    start = time.time()
    for file in filenames:
        read_info(file)
    print(f'Линейный {time.strftime("%H:%M:%S", time.gmtime(time.time() - start))}')

# Многопроцессный
    start = time.time()
    with Pool(5) as p:
        p.map(read_info, filenames)
    print(f'Многопроцессный {time.strftime("%H:%M:%S", time.gmtime(time.time() - start))}')