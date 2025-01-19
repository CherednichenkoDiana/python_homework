import threading
from random import randint
from time import sleep

class Bank:
    def __init__(self,):
        self.balance = 500
        self.lock = threading.Lock()

    def deposit(self):
        tran = 100
        while tran:
            num = randint(50,500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += num
            print(f'Пополнение: {num}. Баланс: {self.balance}')
            sleep(0.001)
            tran -= 1



    def take(self):
        tran = 100
        while tran:
            num = randint(50,500)
            print(f'Запрос на {num}.')
            if num <= self.balance:
                self.balance -= num
                print(f'Снятие: {num}. Баланс: {self.balance}.')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            tran -= 1

if __name__ == '__main__':
    bk = Bank()

    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')