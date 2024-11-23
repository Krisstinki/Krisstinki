import time
from threading import Thread
import sys

print("======= The Night We Met - Lord Huron ======")


lyrics = [
    (" I had all and then most of you", 0.07),
    ("Some and now none of you", 0.06),
    ("Take me back to the night we met", 0.16),
    ("I don't know what I'm supposed to do", 0.06),
    ("Haunted by the ghost of you", 0.09),
    ("Take me back to the night we met", 0.11)
]
delays = [0, 5.0, 11.0, 17.0, 20.5, 26.0]

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
