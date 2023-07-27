from threading import Event, Thread
import time
from src.controller.controller import Controller
import math
import random
from src.model.status import Status


class Worker:
    worker_event: Event = Event()
    worker_thread: Thread
    status: Status = Status.STOPPED

    # controller = Controller()

    def start_working(self) -> None:

        def task(event: Event) -> None:
            counter: int = 0
            time_data: [int] = list()

            sin_signal_data: [float] = list()
            pwm_signal_data: [float] = list()
            triangle_signal_data: [float] = list()

            flag: bool = False
            triangle_signal_counter: int = 0
            while not event.is_set():
                # print("Task in a game", counter, "s")
                # Controller.update_working_time(counter)
                counter += 1

                sin_signal = 3 * math.sin(math.radians(counter))

                if counter % 100 == 0:
                    flag = not flag
                pwm_signal = flag * 6

                if counter % 300 == 0:
                    triangle_signal_counter = 0
                else:
                    triangle_signal_counter += 6 / 300
                triangle_signal = triangle_signal_counter

                sin_signal += random.random()
                pwm_signal += random.random()
                triangle_signal += random.random()

                if 5 > random.randrange(0, 100):
                    sin_signal += random.randrange(-5, 5)
                    pwm_signal += random.randrange(-5, 5)
                    triangle_signal += random.randrange(-5, 5)

                time_data.append(counter)
                sin_signal_data.append(sin_signal)
                pwm_signal_data.append(pwm_signal)
                triangle_signal_data.append(triangle_signal)
                Controller.update_line_series(data_x=time_data, sin_data=sin_signal_data, pwm_data=pwm_signal_data,
                                              triangle_data=triangle_signal_data)
                # time.sleep(0.01)

        self.worker_event.clear()
        self.worker_thread = Thread(target=task, args=(self.worker_event,), daemon=True)

        self.worker_thread.start()
        self.status = Status.ACTIVE
        print("Thread is started")

    def stop_working(self) -> None:
        if self.worker_thread is not None:
            self.worker_event.set()
            self.status = Status.STOPPED
            print("Thread is stopped")
