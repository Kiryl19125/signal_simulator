from threading import Event, Thread
import multiprocessing
import time
from src.controller.controller import Controller
import math


class Worker:
    worker_event: Event = Event()
    worker_thread: Thread

    # controller = Controller()

    def start_working(self) -> None:

        def task(event: Event) -> None:
            counter: int = 0
            time_data: [int] = list()
            signal_data: [float] = list()
            while not event.is_set():
                # print("Task in a game", counter, "s")
                # Controller.update_working_time(counter)
                counter += 1
                signal = 3 * math.sin(math.radians(counter))
                time_data.append(counter)
                signal_data.append(signal)
                Controller.update_line_series(data_x=time_data, data_y=signal_data)
                time.sleep(0.001)

        self.worker_event.clear()
        self.worker_thread = Thread(target=task, args=(self.worker_event,), daemon=True)

        self.worker_thread.start()
        print("Thread is started")

    def stop_working(self) -> None:
        if self.worker_thread is not None:
            self.worker_event.set()
            print("Thread is stopped")
