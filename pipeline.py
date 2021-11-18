import threading
from queue import Queue
from typing import List, Callable


def job1(input_queue: Queue, output_queue: Queue) -> None:
    pass


def job2(input_queue: Queue, output_queue: Queue) -> None:
    pass


def job3(input_queue: Queue, output_queue: Queue) -> None:
    pass


def pipeline(jobs: List[Callable[[Queue, Queue], None]]) -> None:
    pass


if __name__ == "__main__":
    pipeline(
        [
            job1,
            job2,
            job3,
        ]
    )
