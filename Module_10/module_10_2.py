import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemys = 100
        day = 0
        while enemys:
            day += 1
            enemys -= self.power
            sleep(1)
            print(f'{self.name} сражается {day}..., осталось {enemys} воинов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')

if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print(f'Все битвы закончились!')