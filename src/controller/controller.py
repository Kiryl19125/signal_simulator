from src.view.tags import Tag
import dearpygui.dearpygui as dpg
import time


class Controller:

    @staticmethod
    def update_working_time(value: int) -> None:
        # working_time = str(time.strftime('%H:%M:%S', time.gmtime(value)))
        dpg.set_value(item=Tag.WORKING_TIME, value=value)

    @staticmethod
    def update_line_series(data_x: [float], data_y: [float]) -> None:
        # number_of_samples = dpg.get_value(item=Tag.NUMBER_OF_SAMPLES)
        # dpg.set_value(item=Tag.LINE_SERIES,
        # value=[data_x[-number_of_samples:len(data_x)], data_y[-number_of_samples:len(data_y)]])
        dpg.configure_item(item=Tag.LINE_SERIES, x=data_x, y=data_y)
        dpg.fit_axis_data(axis=Tag.PLOT_X_AXIS)
        dpg.fit_axis_data(axis=Tag.PLOT_Y_AXIS)
