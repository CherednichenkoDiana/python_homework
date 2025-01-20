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
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            if not guest.is_alive():
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty():
            for table in self.tables:
                if (not table.guest is None) and (not table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен')
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
        for table in self.tables:
            while table.guest.is_alive():
                table.guest.join()
            print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
            table.guest = None
            print(f'Стол номер {table.number} свободен')




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