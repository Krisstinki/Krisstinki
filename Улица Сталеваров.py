import time
from threading import Thread
import sys

lyrics = [
    ("По улице Сталеваров", 0.09),
    ("Обнявшись гуляли пары", 0.09),
    ("И мы среди них тоже", 0.09),
    ("Похожи на всех прохожих", 0.09),
    ("Текли реки под мостами", 0.09),
    ("И голос через динамик", 0.09),
    ("Из окон открытых настежь", 0.09),
    ("С тобой обещал нам счастье", 0.09),
]

delays = [0, 4, 8, 12, 16, 20, 24, 28]

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
