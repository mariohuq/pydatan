import time
import random

DELAY = 0.1

def count_up(counter):
    while random.randint(0, 3):
        time.sleep(DELAY)
        print(f"Process Up: {counter}")
        counter += 1
def count_down(counter):
    while random.randint(0, 3):
        time.sleep(DELAY)
        print(f"Process Down: {counter}")
        counter -= 1
        