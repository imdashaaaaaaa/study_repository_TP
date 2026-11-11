# Абстрактный обработчик
class SupportHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler    #следующий в цепочке

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return "Никто не смог обработать запрос"


# Конкретные обработчики
class Operator(SupportHandler):
    def handle(self, request):
        if request == "сброс пароля":
            return f"Оператор решил: {request}"
        return super().handle(request)      #передаём дальше


class SeniorSpecialist(SupportHandler):
    def handle(self, request):
        if request == "возврат денег":
            return f"Старший специалист решил: {request}"
        return super().handle(request)


class Manager(SupportHandler):
    def handle(self, request):
        if request == "жалоба на сервис":
            return f"Менеджер решил: {request}"
        return super().handle(request)


# Тест (использование)
if __name__ == "__main__":
    #Строим цепочку: оператор → старший сппециалист → менеджер
    chain = Operator(SeniorSpecialist(Manager()))

    print(chain.handle("сброс пароля"))         #Оператор решил: сброс пароля
    print(chain.handle("возврат денег"))        #Старший специалист решил: возврат денег
    print(chain.handle("жалоба на сервис"))     #Менеджер решил: жалоба на сервис
    print(chain.handle("что-то странное"))      #Никто не смог обработать запрос