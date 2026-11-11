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