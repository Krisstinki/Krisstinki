import time
from threading import Thread
import sys

lyrics = [
    ("Как, как долго не спать, как долго страдать", 0.09),
    ("И не делать уроки", 0.09),
    ("Мама с папой в шоке, ведь я уроки", 0.09),
    ("Делала всегда исправно на пятёрки", 0.08),
    ("Гори, твоё фото", 0.1),
    ("Гори, всё что ты мне дарил", 0.09),
    ("Я не буду скучать", 0.09),
    ("Гори, твоё фото", 0.1),
    ("Гори, всё что ты мне дарил", 0.09),
    ("Я хочу закричать", 0.1)
]

delays = [0, 5.0, 11.0, 17.0, 20.8, 25.0, 30.0, 35.0, 40.0, 45.0]

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
