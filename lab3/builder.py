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
