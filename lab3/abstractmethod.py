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