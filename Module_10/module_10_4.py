import threading
from queue import Queue
from random import randint
from time import sleep

class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        delay = randint(3,10)
        sleep(delay)

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = []
        for tab in tables:
            self.tables.append(tab)

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest == None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                else:
                    self.queue.put(guest)
                    print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while

if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()