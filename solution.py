import threading
import time
from queue import Queue
from typing import List, Callable


def inputs(_: Queue, out_queue: Queue) -> None:
    while True:
        val = input("Enter the integer value\n")

        try:
            val = int(val)
        except ValueError:
            print("Please enter an integer")
        else:
            out_queue.put(item=val)


def square(in_queue: Queue, out_queue: Queue) -> None:
    while True:
        val = in_queue.get()
        out_queue.put(item=val ** 2)
        in_queue.task_done()


def sub(in_queue: Queue, out_queue: Queue) -> None:
    while True:
        val = in_queue.get()
        time.sleep(1)
        out_queue.put(val - 1)
        in_queue.task_done()


def prints(in_queue: Queue, _: Queue) -> None:
    while True:
        print("Output ", in_queue.get())
        in_queue.task_done()


def pipeline(jobs: List[Callable[[Queue, Queue], None]]) -> None:
    threads = []
    in_queue = Queue()

    for job in jobs:
        out_queue = Queue()

        thread = threading.Thread(target=job, args=(in_queue, out_queue), daemon=True)
        threads.append(thread)

        in_queue = out_queue

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    pipeline(
        [
            inputs,
            square,
            sub,
            prints,
        ]
    )
