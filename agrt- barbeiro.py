# Problema do Barbeiro Dorminhoco
def sleeping_barber():
    import threading
    import time

    class BarberShop:
        def __init__(self, num_chairs):
            self.num_chairs = num_chairs
            self.waiting_customers = 0
            self.barber_ready = threading.Semaphore(0)
            self.customer_ready = threading.Semaphore(0)

        def get_haircut(self):
            print("Cliente está cortando cabelo.")
            time.sleep(1)
            print("Cliente terminou o corte de cabelo.")

        def customer(self):
            if self.waiting_customers < self.num_chairs:
                self.waiting_customers += 1
                print("Cliente sentou para esperar.")
                self.customer_ready.release()
                self.barber_ready.acquire()
                self.get_haircut()
            else:
                print("Cliente foi embora porque não há cadeiras disponíveis.")

        def barber(self):
            while True:
                self.customer_ready.acquire()
                self.waiting_customers -= 1
                print("Barbeiro está cortando cabelo.")
                time.sleep(1)
                print("Barbeiro terminou o corte de cabelo.")
                self.barber_ready.release()

    shop = BarberShop(num_chairs=3)
    barber_thread = threading.Thread(target=shop.barber)
    barber_thread.daemon = True
    barber_thread.start()

    customers = [threading.Thread(target=shop.customer) for _ in range(10)]
    for customer in customers:
        customer.start()
        time.sleep(0.5)

    for customer in customers:
        customer.join()