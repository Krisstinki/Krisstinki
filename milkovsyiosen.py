import time
from threading import Thread
import sys

lyrics = [
    ("Молчи, молчи", 0.09),
    ("Я всё уже знаю, я знаю", 0.09),
    ("Ключи, стучи", 0.09),
    ("Я не открываю, я не открываю", 0.09),
    ("А в городе осень, без сна", 0.09),
    ("Что ты меня бросишь, я знал", 0.09),
    ("Я закрываю, глаза закрываю", 0.09),
    ("Но всё-таки будет весна", 0.1),
    ("И ты мне уже не нужна", 0.1),
    ("И я забываю, тебя забываю", 0.1),
]

delays = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]

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
