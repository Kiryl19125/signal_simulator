from threading import Event, Thread
import multiprocessing
import time
from src.controller.controller import Controller


class Worker:
    worker_event: Event = Event()
    worker_thread: Thread

    # controller = Controller()

    def start_working(self) -> None:

        def task(event: Event) -> None:
            counter: int = 0
            while not event.is_set():
                print("Task in a game", counter, "s")
                Controller.update_working_time(counter)
                counter += 1
                time.sleep(1)

        self.worker_thread = Thread(target=task, args=(self.worker_event,), daemon=True)

        self.worker_thread.start()
        print("Thread is started")

    def stop_working(self) -> None:
        if self.worker_thread is not None:
            self.worker_event.set()
            print("Thread is stopped")


class Plotting:
    plotting_event: Event = Event()
    plotting_thread: Thread

    def start_plotting(self) -> None:
        def gen_signal(event: Event) -> None:
            data_x: [float] = list()
            data_y: [float] = list()
            # time_0 = time.time()
            counter: int = 0
            while not event.is_set():
                # current_time = time.time() - time_0
                # # working_time = time.strftime("%H:%M:%S", time.gmtime(current_time))
                # data_x.append(current_time)
                # data_y.append(3)
                counter += 1
                data_x.append(counter)
                data_y.append(counter)
                Controller.update_line_series(data_x, data_y)
                time.sleep(0.1)

        self.plotting_thread = Thread(target=gen_signal, args=(self.plotting_event,))
        self.plotting_thread.start()
        print("Plotting thread starter")

    def stop_plotting(self) -> None:
        if self.plotting_thread is not None:
            self.plotting_event.set()
            print("Plotting thread stopped")
