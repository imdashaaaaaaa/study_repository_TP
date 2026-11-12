# Порождающие паттерны проектирования - определяют как создавать объекты "по чертежу"

## Builder (строитель) 
### Выносит общую логику создания целевого финального класса в отдельную сущность 
``` python
# Product
class Coffee:
    ##Кофе (то что мы собираем)

    def __init__(self):
        self._size = None
        self._beans = None
        self._milk = None

    def set_size(self, size):
        self._size = size

    def set_beans(self, beans):
        self._beans = beans

    def set_milk(self, milk):
        self._milk = milk

    def __str__(self):
        return f"Coffee(size={self._size}, beans={self._beans}, milk={self._milk})"


# Builder
class CoffeeBuilder:
    #Договор (инструкция) какие шаги обязательны при сборке кофе

    def build_size(self): ...
    def build_beans(self): ...
    def build_milk(self): ...
    def get_result(self): ...


# Concrate Builder (Latte)
class LatteBuilder(CoffeeBuilder):
    #Строитель латте, знает свой рецепт

    def __init__(self):
        self.coffee = Coffee()

    def build_size(self):
        self.coffee.set_size("средний")

    def build_beans(self):
        self.coffee.set_beans("арабика")

    def build_milk(self):
        self.coffee.set_milk("обычное")

    def get_result(self):
        return self.coffee


# Concrate Builder (Cappuccino)
class CappuccinoBuilder(CoffeeBuilder):
    #Строитель капучино, знает свой рецепт

    def __init__(self):
        self.coffee = Coffee()

    def build_size(self):
        self.coffee.set_size("большой")

    def build_beans(self):
        self.coffee.set_beans("смесь")

    def build_milk(self):
        self.coffee.set_milk("вспененное")

    def get_result(self):
        return self.coffee


# Director
class CoffeeDirector:
    #Директор знает только порядок шагов, не знает какой именно кофе

    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_size()
        self.builder.build_beans()
        self.builder.build_milk()


# Тест (использование)
if __name__ == "__main__":
    #Латте
    latte_builder = LatteBuilder()
    director = CoffeeDirector(latte_builder)
    director.construct()
    print("Латте:", latte_builder.get_result())

    #Капучино (тот же директор, другой строитель)
    capp_builder = CappuccinoBuilder()
    director = CoffeeDirector(capp_builder)   #только эта строка меняется
    director.construct()
    print("Капучино:", capp_builder.get_result())
```

## Factory Method (фабричный метод) 
### Определяет интерфейс для создания объекта, но позволяет подклассам изменять тип создаваемого объекта
### Клиент: "Дай мне 1 вещь, сам реши какую" *

``` python
# Абстрактный продукт (транспорт)
``` python
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
```

## Abstract Factory (абстрактная фабрика) 
### Предоставляет интерфейс для создания множества взаимосвязанных или взаимозависимых объектов, независимо от их конкретных реализаций
### Клиент: "Дай мне набор вещей которые сочетаются друг с другом" *
``` python
# Абстрактные продукты
class Warrior:
    def attack(self): ...

class Archer:
    def shoot(self): ...

class Mage:
    def cast_spell(self): ...


# Эльфийские персонажи
class ElfWarrior(Warrior):
    def attack(self):
        print("Эльф-воин бьёт точно в цель")

class ElfArcher(Archer):
    def shoot(self):
        print("Эльф-лучник стреляет из лука")

class ElfMage(Mage):
    def cast_spell(self):
        print("Эльф-маг лечит союзников")


# Оркские персонажи
class OrcWarrior(Warrior):
    def attack(self):
        print("Орк-воин бьёт топором")

class OrcArcher(Archer):
    def shoot(self):
        print("Орк-лучник кидает копьё")

class OrcMage(Mage):
    def cast_spell(self):
        print("Орк-маг кидает огненный шар")


# Абстрактная фабрика
class ArmyFactory:
    ##Создаёт целый набор персонажей (юнитов) одной расы

    def create_warrior(self): ...
    def create_archer(self): ...
    def create_mage(self): ...


# Конкретные фабрики
class ElfArmyFactory(ArmyFactory):
    def create_warrior(self): return ElfWarrior()
    def create_archer(self):  return ElfArcher()
    def create_mage(self):    return ElfMage()


class OrcArmyFactory(ArmyFactory):
    def create_warrior(self): return OrcWarrior()
    def create_archer(self):  return OrcArcher()
    def create_mage(self):    return OrcMage()


# Клиенты
def build_army(factory: ArmyFactory):
    ##Клиент: работает с любой армией, не зная расы
    return [
        factory.create_warrior(),
        factory.create_archer(),
        factory.create_mage(),
    ]


def show_army(army):
    print("Армия:")
    for unit in army:
        if isinstance(unit, Warrior):
            unit.attack()
        elif isinstance(unit, Archer):
            unit.shoot()
        elif isinstance(unit, Mage):
            unit.cast_spell()


# Тест (использование)
if __name__ == "__main__":
    print("Эльфийская армия:")
    show_army(build_army(ElfArmyFactory()))

    print("\nОркская армия:")
    show_army(build_army(OrcArmyFactory()))
```

## Singleton (одиночка)
### Гарантирует, что у класса есть только один экземпляр, и предоставляет глобальную точку доступа к этому экземпляру.
``` python
import threading


class AppConfig:
    ##Потокобезопасный Singleton: настройки приложения

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        ##Первая проверка без блокировки (скорость)
        if cls._instance is None:
            with cls._lock:
                #Вторая проверка внутри блокировки (корректность)
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.settings = {}
        self._initialized = True

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key, default=None):
        return self.settings.get(key, default)

# Тест (использование)
if __name__ == "__main__":
    ##Один и тот же экземпляр
    a = AppConfig()
    b = AppConfig()
    print("a is b:", a is b)      #true

    ##Настройки общие
    a.set("theme", "dark")
    print("b.get('theme'):", b.get("theme"))  #dark
    print("b.get('language'):", b.get("language", "ru")) #ru (default)
```

