from abc import ABC, abstractmethod

# ==========================================
# 1. ИНТЕРФЕЙСЫ (Умения)
# ==========================================
# В Python интерфейсы реализуются через ABC (Абстрактные Базовые Классы)
# с абстрактными методами.

class Attacker(ABC):
    """Интерфейс для тех, кто умеет атаковать"""
    @abstractmethod
    def attack(self, unit: 'Unit'):
        pass

class Moveable(ABC):
    """Интерфейс для тех, кто умеет двигаться"""
    @abstractmethod
    def move(self, x: int, y: int):
        pass


# ==========================================
# 2. БАЗОВЫЕ КЛАССЫ (Иерархия)
# ==========================================

class GameObject(ABC):
    """Базовый класс для всех объектов в игре"""
    def __init__(self, id: int, name: str, x: int, y: int):
        self._id = id
        self._name = name
        self._x = x
        self._y = y

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y


class Unit(GameObject):
    """Класс для юнитов (живых существ)"""
    def __init__(self, id: int, name: str, x: int, y: int, hp: float):
        super().__init__(id, name, x, y)
        self._hp = hp

    def is_alive(self) -> bool:
        return self._hp > 0

    def get_hp(self) -> float:
        return self._hp

    def receive_damage(self, damage: float):
        self._hp -= damage
        if self._hp < 0:
            self._hp = 0
        print(f"  [{self._name}] получил {damage} урона. Осталось HP: {self._hp:.1f}")


class Building(GameObject):
    """Класс для построек"""
    def __init__(self, id: int, name: str, x: int, y: int, is_built: bool):
        super().__init__(id, name, x, y)
        self._is_built = is_built

    def is_built(self) -> bool:
        return self._is_built


# ==========================================
# 3. КОНКРЕТНЫЕ КЛАССЫ (Реализация)
# ==========================================

class Archer(Unit, Attacker, Moveable):
    """Лучник: юнит, который умеет и атаковать, и двигаться"""
    def attack(self, unit: Unit):
        if not unit.is_alive():
            print(f"  {unit.get_name()} уже мертв, атака невозможна.")
            return
        damage = 15.0
        print(f"🏹 {self.get_name()} стреляет в {unit.get_name()}!")
        unit.receive_damage(damage)

    def move(self, x: int, y: int):
        print(f"🏃 {self.get_name()} перемещается на координаты ({x}, {y}).")
        self._x = x
        self._y = y


class Fort(Building, Attacker):
    """Крепость: постройка, которая умеет ТОЛЬКО атаковать"""
    def attack(self, unit: Unit):
        if not self.is_built():
            print(f"🏰 {self.get_name()} еще не построена, стрелять нельзя!")
            return
        if not unit.is_alive():
            print(f"  {unit.get_name()} уже мертв, атака невозможна.")
            return
        damage = 50.0
        print(f"💥 {self.get_name()} стреляет из пушки в {unit.get_name()}!")
        unit.receive_damage(damage)


class MobileHouse(Building, Moveable):
    """Дом на колесах: постройка, которая умеет ТОЛЬКО двигаться"""
    def move(self, x: int, y: int):
        if not self.is_built():
            print(f"🏠 {self.get_name()} еще не достроен, он не может ехать.")
            return
        print(f"🚐 {self.get_name()} медленно катится на координаты ({x}, {y}).")
        self._x = x
        self._y = y


# ==========================================
# 4. ПРОВЕРКА РАБОТЫ (Тесты)
# ==========================================
if __name__ == "__main__":
    print("--- Создание объектов ---")
    archer1 = Archer(1, "Леголас", 10, 10, 100)
    archer2 = Archer(2, "Враг", 20, 20, 50)
    fort = Fort(3, "Крепость", 0, 0, True) # Построена
    house = MobileHouse(4, "Дом на колесах", 5, 5, True) # Достроен
    
    print("\n--- Начало битвы ---")
    archer1.attack(archer2) # Лучник 1 атакует Лучника 2
    archer2.attack(archer1) # Лучник 2 отвечает
    fort.attack(archer1)    # Крепость стреляет по Лучнику 1
    
    print("\n--- Движение ---")
    archer1.move(15, 15)    # Лучник двигается
    house.move(10, 10)      # Дом на колесах двигается
    
    print("\n--- Проверка на мертвого юнита ---")
    archer1.attack(archer2) # Добиваем Лучника 2 (у него было 35 HP после первой атаки, 15 урона не хватит, чтобы убить, поэтому атакуем еще раз)
    fort.attack(archer2)    # Крепость добивает (50 урона)
    archer1.attack(archer2) # Пытаемся атаковать мертвого