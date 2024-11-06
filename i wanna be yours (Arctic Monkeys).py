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
        ("\n""Secrets I have held in my heart", 0.08),
        ("Are harder to hide than I thought", 0.08),
        ("Maybe I just wanna be yours", 0.08),
        ("I wanna be yours, I wanna be yours", 0.08),
        ("Wanna be yours", 0.08),
        ("Wanna be yours", 0.08),
        ("Wanna be yours", 0.08),
    ]
    
    delays = [0.5, 3.0, 5.5, 8.0, 10.5, 12.0, 13.5]  # Adjusted to have some timing between lines

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
