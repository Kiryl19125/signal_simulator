from enum import Enum, auto, unique


@unique
class Tag(str, Enum):
    SETTINGS_WINDOW = auto()
    QUIT_BUTTON = auto()
    PLOT_WINDOW = auto()
    CONSOLE_WINDOW = auto()
    CONSOLE = auto()
    COMMEND_INPUT = auto()
    SEND_COMMEND_BUTTON = auto()
    AUTOSCROLL_CHECKBOX = auto()
    PLOT = auto()
    PLOT_X_AXIS = auto()
    PLOT_Y_AXIS = auto()
    LINE_SERIES = auto()
    FIT_X_AXIS = auto()
    FIT_Y_AXIS = auto()
    NUMBER_OF_SAMPLES = auto()
    SHOW_HIDE_CONSOLE = auto()
    HEADER = auto()
    CONNECTION_TAB = auto()
    SIMULATION_TAB = auto()
    START_SIMULATION_BUTTON = auto()
    STOP_SIMULATION_BUTTON = auto()
    WORKING_TIME = auto()
