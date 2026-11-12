# Структурные паттерны проектирования - описывают как классы и объекты могут быть составлены в более крупные структуры, обеспечивая при этом гибкость и масштабируемость

## Proxy - предоставляет суррогатный объект вместо реального (заместитесь с тем же интерфейсом)
### Управляет доступом к реальному объекту, добавляя свою логику
### 1) Ленивая загрузка
### 2) Кеширование
### 3) Контроль доступа
``` python
# Общий интерфейс для реального видео и прокси (субъект)
class Video:
    def play(self):
        ...


# Реальное видео: тяжёлая загрузка при создании
class RealVideo(Video):
    def __init__(self, filename):
        self.filename = filename
        print(f"[RealVideo] загружаю видео '{filename}' (это долго...)")

    def play(self):
        print(f"[RealVideo] воспроизвожу '{self.filename}'")


# Прокси: ленивая загрузка + кеш
class VideoProxy(Video):
    def __init__(self, filename):
        self.filename = filename
        self._real_video = None

    def play(self):
        #Создаём реальное видео только при первом вызове
        if self._real_video is None:
            self._real_video = RealVideo(self.filename)
        #Повторно не загружаем, используем то же видео
        self._real_video.play()


if __name__ == "__main__":
    print("Создаю прокси (видео ещё не загружено)")
    video = VideoProxy("movie.mp4")

    print("\nПервый play - загрузка")
    video.play()

    print("\nВторой play - из кеша, загрузки нет")
    video.play()
```

## Adapter (переходник) - позволяет объектам с несовместимыми интерфейсами работать вместе
### Оборачивает объект одного интерфейса и переводит в формат, понятный другому интерфейсу
### 1) Переводы и оплата в разных валюах
### 2) Работа с внешними API 
### 3) Интер=грация с устаревшими форматами и библиотеками
### 4) Разные форматы источников данных
``` python
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
```

## Bridge (мост) - разделяет абстракцию (интерфейс) и реализацию (конкретные детали) на разные иерархии, чтобы их можно было изменять независимо
### Добавляет расширенную абстракцию
### 1) Архитектура должна поддерживать разные группировки
``` python
# Интерфейс формата экспорта: в каком формате выводим
class ExportFormat:
    def export(self, data):
        ...


# Конкретные форматы
class PdfFormat(ExportFormat):
    def export(self, data):
        print(f"PDF сохраняю отчёт: {data}")


class ExcelFormat(ExportFormat):
    def export(self, data):
        print(f"Excel сохраняю отчёт: {data}")


class CsvFormat(ExportFormat):
    def export(self, data):
        print(f"CSV сохраняю отчёт: {data}")


# Базовый отчёт: хранит ссылку на формат
class Report:
    def __init__(self, export_format):
        self.export_format = export_format

    def generate(self):
        # Готовим данные — каждый отчёт по-своему
        data = self.prepare_data()
        # Делегируем экспорт формату
        self.export_format.export(data)

    def prepare_data(self):
        ...


# Расширенные отчёты
class SalesReport(Report):
    def prepare_data(self):
        return "Отчёт по продажам: 1500 заказов, 2 млн руб."


class WarehouseReport(Report):
    def prepare_data(self):
        return "Отчёт по складу: 300 позиций, 50 на исходе"


class ClientsReport(Report):
    def prepare_data(self):
        return "Отчёт по клиентам: 1200 клиентов, 150 новых"


if __name__ == "__main__":
    #Отчёт по продажам в PDF
    sales_pdf = SalesReport(PdfFormat())
    sales_pdf.generate()

    #Тот же отчёт в Excel
    sales_excel = SalesReport(ExcelFormat())
    sales_excel.generate()

    #Отчёт по складу в CSV
    warehouse_csv = WarehouseReport(CsvFormat())
    warehouse_csv.generate()

    #Отчёт по клиентам в PDF
    clients_pdf = ClientsReport(PdfFormat())
    clients_pdf.generate()
```
