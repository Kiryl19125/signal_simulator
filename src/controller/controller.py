from src.view.tags import Tag
import dearpygui.dearpygui as dpg
from config.default import Default


class Controller:

    @staticmethod
    def update_working_time(value: int) -> None:
        if dpg.is_dearpygui_running():
            dpg.set_value(item=Tag.WORKING_TIME, value=value)

    @staticmethod
    def update_line_series(data_x: [float], data_y: [float]) -> None:
        # number_of_samples = dpg.get_value(item=Tag.NUMBER_OF_SAMPLES)
        # dpg.set_value(item=Tag.LINE_SERIES,
        # value=[data_x[-number_of_samples:len(data_x)], data_y[-number_of_samples:len(data_y)]])
        if dpg.is_dearpygui_running():
            try:
                # data_x = data_x[-Default.MAX_NUMBER_OF_SAMPLES:]
                # data_y = data_y[-Default.MAX_NUMBER_OF_SAMPLES:]
                # dpg.configure_item(item=Tag.LINE_SERIES, x=data_x, y=data_y)
                dpg.set_value(item=Tag.LINE_SERIES,
                              value=[data_x[-dpg.get_value(item=Tag.NUMBER_OF_SAMPLES):len(data_x)],
                                     data_y[-dpg.get_value(item=Tag.NUMBER_OF_SAMPLES):len(data_y)]])

                if dpg.get_value(item=Tag.FIT_X_AXIS):
                    dpg.fit_axis_data(axis=Tag.PLOT_X_AXIS)
                if dpg.get_value(item=Tag.FIT_Y_AXIS):
                    dpg.fit_axis_data(axis=Tag.PLOT_Y_AXIS)
            except Exception as e:
                print("Something went wrong Exception: ", e)
