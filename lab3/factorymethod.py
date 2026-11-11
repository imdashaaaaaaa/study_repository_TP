# Абстрактный продукт (транспорт)
class Transport:
    ##Общий договор для всех видов транспорта

    def deliver(self, cargo):
        ...


# Конкретные продукты (виды транспорта)
class Truck(Transport):
    ##Грузовик: доставляет по земле

    def deliver(self, cargo):
        print(f"Грузовик доставляет '{cargo}' по земле")


class Ship(Transport):
    ##Корабль: доставляет по морю

    def deliver(self, cargo):
        print(f"Корабль доставляет '{cargo}' по морю")


class Plane(Transport):
    ##Самолёт: доставляет по воздуху

    def deliver(self, cargo):
        print(f"Самолёт доставляет '{cargo}' по воздуху")


# Абстрактный создатель
class Logistics:
    ##Общий договор для всех видов логистики

    def create_transport(self):
        ...

    def plan_delivery(self, cargo):
        ##Общий алгоритм доставки, работает для любой логистики
        transport = self.create_transport()
        print(f"Планирую доставку груза '{cargo}'...")
        transport.deliver(cargo)


# Конкретные создатели
class RoadLogistics(Logistics):
    ##Наземная логистика - создаёт грузовик

    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):
    ##Морская логистика - создаёт корабль

    def create_transport(self):
        return Ship()


class AirLogistics(Logistics):
    ##Воздушная логистика - создаёт самолёт

    def create_transport(self):
        return Plane()


# Тест (использование)
if __name__ == "__main__":
    #Наземная доставка
    road = RoadLogistics()
    road.plan_delivery("Ноутбуки")

    #Морская доставка
    sea = SeaLogistics()
    sea.plan_delivery("Контейнеры")

    #Воздушная доставка
    air = AirLogistics()
    air.plan_delivery("Цветы")