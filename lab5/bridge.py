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