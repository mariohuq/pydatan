import os
from multiprocessing import Queue

def worker(tasks: Queue, process_index: int):
    def fib(n: int) -> int:
        return fib(n-1) + fib(n-2) if n > 2 else 1
    
    while not tasks.empty():  # пока очередь не пуста выполняем одну очередную задачу
        number = tasks.get()
        answer = fib(number)
        print(f"worker {process_index}, PID={os.getpid()}: fib({number}) = {answer}")