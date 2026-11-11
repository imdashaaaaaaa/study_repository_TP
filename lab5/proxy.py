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