from threading import Thread
from multiprocessing import Process
from random import randint
from time import time
from typing import Optional
from typing import Callable
from typing import Union


class MyFunc:
    def __init__(self, func: Callable, arg) -> None:
        self.func = func
        self.arg = arg

    def start(self) -> None:
        self.func(self.arg)

    def join(self) -> None:
        pass


def fib(n: int) -> Optional[int]:
    f1, f2 = 0, 1

    if n < 0:
        return None

    if n < 2:
        return [f1, f2][n]

    for _ in range(1, n):
        f1, f2 = f2, f1 + f2

    return f2


def run_objects_with_timer(objects: list[Union[Thread, Process, MyFunc]]) -> float:
    time_start = time()

    [object.start() for object in objects]
    [object.join() for object in objects]

    return time() - time_start


if __name__ == "__main__":
    amount_of_tests = 10

    num_lower_bound = 1e4
    num_upper_bound = 1e6

    random_numbers = [
        randint(num_lower_bound, num_upper_bound) for _ in range(amount_of_tests)
    ]

    threads = [Thread(target=fib, args=(x,)) for x in random_numbers]
    processes = [Process(target=fib, args=(x,)) for x in random_numbers]
    synchronized = [MyFunc(fib, x) for x in random_numbers]

    threads_time = run_objects_with_timer(threads)
    processed_time = run_objects_with_timer(processes)
    synchronized = run_objects_with_timer(synchronized)

    with open("time_complecity.txt", "w") as file:
        column_of_nums = "\n\t".join([str(x) for x in random_numbers])
        
        print(f"fib_n: [\n\t{column_of_nums}\n]", file=file)
        print(f"threads_time={threads_time} sec", file=file)
        print(f"processed_time={processed_time} sec", file=file)
        print(f"synchronized={synchronized} sec", file=file)
