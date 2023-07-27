import dearpygui.dearpygui as dpg
from src.view.tags import Tag


class Tooltip:

    @staticmethod
    def create_tooltips() -> None:
        with dpg.tooltip(parent=Tag.STOP_SIMULATION_BUTTON):
            dpg.add_text("This button will stop simulation")

        with dpg.tooltip(parent=Tag.START_SIMULATION_BUTTON):
            dpg.add_text("This button will start simulation")

        with dpg.tooltip(parent=Tag.FIT_Y_AXIS):
            dpg.add_text("Fit everything in Y axis")

        with dpg.tooltip(parent=Tag.FIT_X_AXIS):
            dpg.add_text("Fit everything in X axis")
