import time
from threading import Thread, Lock
import sys
from colorama import init, Fore, Style 

# Initialize colorama
init()

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
    RED = Fore.RED
    RESET = Style.RESET_ALL

    lyrics = [
        (f"I have {RED}loved{RESET} you since we were {RED}18{RESET}", 0.08),
        (f"Long before we both thought the {RED}same thing{RESET}", 0.07),
        (f"To be {RED}loved{RESET} and to be {RED}in love{RESET}", 0.07),
        (f"And all I could do is say that these arms were made for {RED}holding you{RESET} oh oh oh whoa", 0.07),
        (f"I wanna {RED}love{RESET} like you made me feel", 0.09),
        (f"When we were {RED}18{RESET}", 0.1)
    ]
    delays = [0.3, 6.9, 11.0, 14.0, 20.8, 24.8]
    
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
