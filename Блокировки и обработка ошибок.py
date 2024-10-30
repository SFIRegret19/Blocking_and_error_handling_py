import threading
import random
import time

class Bank:
    def __init__(self, balance):
        self.__lock = threading.Lock()
        self.balance = balance
        self.__transactions = 100

    def deposit(self):
        if self.balance >= 500 and self.__lock.locked() == True:
                self.__lock.release()
        for _ in range(self.__transactions):
            dep = random.randint(50,500)
            self.balance += dep
            print(f'Пополнение: {dep}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(self.__transactions):
            withdrawal = random.randint(50,500)
            print(f'Запрос на {withdrawal}')
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f'Снятие: {withdrawal}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.__lock.acquire()
            time.sleep(0.001)

bk = Bank(1000)

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')