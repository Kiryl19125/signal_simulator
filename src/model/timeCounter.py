from threading import Event, Thread
import time
from src.controller.controller import Controller

class TimeCounter:
    event: Event = Event()
    thread: Thread

    def start(self) -> None:

        def task(event: Event) -> None:
            pass