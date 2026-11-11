# Стратегия (интерфейс)
class PaymentStrategy:
    def pay(self, amount):
        ...


# Конкретная стратегия
class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Карта оплачено {amount} руб.")


class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Наличные оплачено {amount} руб.")


class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Крипта оплачено {amount} руб.")


# Контекст
class Order:
    def __init__(self, amount, strategy: PaymentStrategy):
        self.amount = amount
        self.strategy = strategy          #храним стратегию

    def checkout(self):
        self.strategy.pay(self.amount)    #вызываем стратегию


# Тест (использование)
if __name__ == "__main__":
    order1 = Order(1500, CardPayment())
    order1.checkout()                     #Карта оплачено 1500 руб.

    order2 = Order(800, CashPayment())
    order2.checkout()                     #Наличные оплачено 800 руб.

    order3 = Order(3000, CryptoPayment())
    order3.checkout()                     #Крипта оплачено 3000 руб.