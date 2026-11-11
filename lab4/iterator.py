# Итератор
class BookShelfIterator:
    def __init__(self, shelf):
        self.shelf = shelf
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.shelf.books):
            raise StopIteration            #сигнал, элементы закончились
        book = self.shelf.books[self.index]
        self.index += 1
        return book


# Коллекция (книжный шкаф)
class BookShelf:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def __iter__(self):
        return BookShelfIterator(self)     # создаём итератор


# Тест (использование)
if __name__ == "__main__":
    shelf = BookShelf()
    shelf.add("Война и мир")
    shelf.add("Преступление и наказание")
    shelf.add("Мастер и Маргарита")

    iterator = iter(shelf)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

## Или через for (обязательно своя итерация, т.к. питон не знает как проходить конкретно мой класс
    for book in shelf:
        print(f"Книга: {book}")
