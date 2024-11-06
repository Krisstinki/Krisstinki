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
        ("\n""With the lights out, it's less dangerous", 0.08),
        ("Here we are now, entertain us", 0.08),
        ("I feel stupid and contagious", 0.08),
        ("Here we are now, entertain us", 0.08),
        ("A mulatto, an albino", 0.08),
        ("A mosquito, my libido", 0.08),
        ("Yeah", 0.1),
        ("Hey", 0.1),
        ("Yay", 0.1)
    ]
    
    delays = [0.5, 3.0, 5.5, 8.0, 10.5, 12.5, 14.5, 16.0, 17.0]  # Timed delays for each line

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
