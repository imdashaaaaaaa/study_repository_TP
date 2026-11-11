# Интерфейс, который ожидает наш код
class PaymentGateway:
    def pay(self, amount):
        ...


# Старая система: работает с копейками и валютой
class OldPaymentSystem:
    def make_payment(self, sum_kopecks, currency):
        print(f"(OldPaymentSystem) оплата {sum_kopecks} {currency}")
        return True


# Адаптер: переводит pay(amount) в make_payment(sum_kopecks, currency)
class PaymentAdapter(PaymentGateway):
    def __init__(self, old_system):
        self.old_system = old_system

    def pay(self, amount):
        # Переводим рубли в копейки
        sum_kopecks = amount * 100
        # Вызываем старую систему
        return self.old_system.make_payment(sum_kopecks, "RUB")


# Клиент работает с PaymentGateway (не знает про адаптер)
def checkout(gateway, amount):
    print(f"Оформляю заказ на {amount} руб.")
    success = gateway.pay(amount)
    print("Оплата прошла" if success else "Оплата не прошла")


if __name__ == "__main__":
    old_system = OldPaymentSystem()
    adapter = PaymentAdapter(old_system)

    checkout(adapter, 1500)
    checkout(adapter, 300)