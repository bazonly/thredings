import random
import threading
import time


class Supermart:
    def __init__(self):
        self.client_count = threading.Semaphore(4)
        self.cash = random.randint(1000, 10000)
        self.payment_methods = ['card', 'cash']

    def meet_client(self, client):
        print(f'\nприглашаем к кассе {client} покупателя')
        self.client_count.acquire()

        print(f'\nработаем с {client} покупателем')
        payment_method = random.choice(self.payment_methods)
        price = random.randint(10000, 100000)
        time.sleep(5)
        if payment_method != 'card':
            if price > self.cash:
                print('\nГАЛЯЯЯЯЯ!!!')
                time.sleep(10)
                self.cash = self.cash + random.randint(price, 10000000) - price
            else:
                self.cash -= price

        print(f'\nзавершаем работу с {client} покупателем')
        self.client_count.release()

    def clients(self, count: int):

        for client in range(1, count + 1):
            client_thread = threading.Thread(target = self.meet_client, args=(client,))
            client_thread.start()


if __name__ == '__main__':
    Clients = Supermart()
    count = 10
    Clients.clients(count)
