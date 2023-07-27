# import threading
# import enum
#
#
# class State(enum.Flag):
#     ACTIVE = True
#     STOPPED = False
#
#
# class MainApp:
#     _state: State
#     _cancel: threading.Event()
#     _worker: threading.Thread
#
#     def get_state(self) -> State:
#         return self._state
#
#     def _get_worker(self) -> threading.Thread:
#         def loop():
#             while State.ACTIVE.value:
#                 print("Working")
#
#         return threading.Thread(target=loop, daemon=True)
#
#     def start(self):
#         self._state = State.ACTIVE
#
#     def stop(self):
#         self._state = State.STOPPED


from src.model.worker import Worker
from src.model.worker import Plotting


class MainApp:
    main_worker: Worker = Worker()
    plotting_worker: Plotting = Plotting()

    def start_button_callback(self):
        # self.plotting_worker.flag = True
        # print("Start button was pressed")
        self.plotting_worker.start_plotting()

    def stop_button_callback(self):
        # print("Stop button was pressed")
        # self.plotting_worker.flag = False
        self.plotting_worker.stop_plotting()
