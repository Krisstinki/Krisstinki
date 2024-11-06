import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\n""How I wine pon you", 0.08),
        ("The way I wine pon you", 0.08),
        ("How I wine pon you", 0.08),
        ("The way I wine pon you, yeah", 0.08),
        ("Take it, you just like the way I wine pon you", 0.08),
        ("Take it, you just like the way I wine pon you, yeah", 0.08)
    ]
    
    delays = [0.5, 2.5, 5.0, 7.5, 10.0, 12.5]  # Timing delays for each line

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
