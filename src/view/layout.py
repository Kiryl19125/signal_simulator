import dearpygui.dearpygui as dpg
from dearpygui_ext.themes import create_theme_imgui_dark, create_theme_imgui_light
from src.view.tags import Tag
from typing import Callable, Final, Iterable, Union, cast
from config.default import Default
from config.config import Config


# class Default:
#     FONT_HEIGHT: int = 24
#     FONT: str = "resources/fonts/falling-sky-font/FallingSky-JKwK.otf"
#     INIT_FILE_PATH: str = "config/dpg.ini"
#     RESIZE_OFFSET: int = 240
#     MIN_NUMBER_OF_SAMPLES = 100
#     MAX_NUMBER_OF_SAMPLES = 10_000


# class Config:
#     WINDOW_CONFIG = dict(no_collapse=True, no_close=True)
#     APP_CONFIG = dict(docking=True, docking_space=True, init_file=Default.INIT_FILE_PATH, load_init_file=True)


class Font:
    DEFAULT: int


class Theme:
    DEFAULT: int
    DARK: int
    LIGHT: int


def _init_theme() -> None:
    ...


def _init_fonts() -> None:
    with dpg.font_registry():
        Font.DEFAULT = dpg.add_font(Default.FONT, Default.FONT_HEIGHT)
    dpg.bind_font(Font.DEFAULT)


def _header() -> None:
    def show_hide_console(sender) -> None:
        if dpg.get_value(item=sender) == "Show":
            dpg.show_item(item=Tag.CONSOLE_WINDOW)
        else:
            dpg.hide_item(item=Tag.CONSOLE_WINDOW)

    with dpg.viewport_menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Open")
            dpg.add_menu_item(label="Save")
            dpg.add_menu_item(label="Save As")
            with dpg.menu(label="Settings"):
                dpg.add_menu_item(label="Style Editor", callback=lambda: dpg.show_style_editor())
                dpg.add_menu_item(label="Font Registry", callback=lambda: dpg.show_font_manager())
            dpg.add_separator()
            dpg.add_menu_item(label="Quit", tag=Tag.QUIT_BUTTON)
        with dpg.menu(label="Options"):
            dpg.add_menu_item(label="Save Window Configuration",
                              callback=lambda: dpg.save_init_file(file=Default.INIT_FILE_PATH))
        with dpg.menu(label="View"):
            with dpg.menu(label="Console"):
                dpg.add_radio_button(items=["Show", "Hide"], tag=Tag.SHOW_HIDE_CONSOLE, callback=show_hide_console,
                                     default_value="Show")
            with dpg.menu(label="Themes"):
                dpg.add_radio_button(items=["Default", "Dark", "Light"])


def _body() -> None:
    with dpg.window(tag=Tag.SETTINGS_WINDOW, label="Setting Window", **Config.WINDOW_CONFIG):
        settings_window()
    with dpg.window(tag=Tag.PLOT_WINDOW, label="Plot Window", **Config.WINDOW_CONFIG):
        plot_window()
    with dpg.window(tag=Tag.CONSOLE_WINDOW, label="Console Window", **Config.WINDOW_CONFIG):
        console_window()


def console_window() -> None:
    with dpg.group(horizontal=True):
        dpg.add_input_text(hint="Type Commend", tag=Tag.COMMEND_INPUT, width=420, tracked=True)
        dpg.add_button(label="Send", width=100, tag=Tag.SEND_COMMEND_BUTTON)
        dpg.add_checkbox(label="Autoscroll", default_value=True, tag=Tag.AUTOSCROLL_CHECKBOX)
    with dpg.child_window(tag=Tag.CONSOLE, width=-1, height=-1):
        pass


def plot_window() -> None:
    with dpg.group(horizontal=True):
        dpg.add_slider_int(label="Data Frame", tag=Tag.NUMBER_OF_SAMPLES,
                           min_value=Default.MIN_NUMBER_OF_SAMPLES, max_value=Default.MAX_NUMBER_OF_SAMPLES,
                           width=420, default_value=Default.MAX_NUMBER_OF_SAMPLES // 2)
        dpg.add_checkbox(label="Fit Y Axis", default_value=True, tag=Tag.FIT_Y_AXIS)
        dpg.add_checkbox(label="Fit X Axis", default_value=True, tag=Tag.FIT_X_AXIS)
        dpg.add_text(tag=Tag.WORKING_TIME)
        dpg.add_text(default_value="s")
    with dpg.plot(label="Sinus", height=-1, width=-1, tag=Tag.PLOT):
        dpg.add_plot_legend()

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="x", tag=Tag.PLOT_X_AXIS)
        dpg.add_plot_axis(dpg.mvYAxis, label="y", tag=Tag.PLOT_Y_AXIS)

        # series belong to a y axis
        dpg.add_line_series(label="sin", parent=Tag.PLOT_Y_AXIS, tag=Tag.LINE_SERIES, x=[], y=[])

        # dpg.set_axis_limits(axis=Tag.PLOT_Y_AXIS, ymin=-5, ymax=5)
        # dpg.set_axis_limits_auto(Tag.)


def settings_window() -> None:
    with dpg.tab_bar(tag=Tag.HEADER):
        with dpg.tab(label="Connection"):
            dpg.add_button(label="Start", width=-1, enabled=False)

        with dpg.tab(label="Simulation"):
            with dpg.group(horizontal=True):
                dpg.add_combo(items=["sin", "cos", "pwm"], label="Signal Type", width=100)
                dpg.add_combo(items=["100 MG", "200 MG", "300 MG"], label="Frequency", width=100)
            dpg.add_separator()
            dpg.add_button(label="Start Simulation", width=-1, tag=Tag.START_SIMULATION_BUTTON)
            dpg.add_button(label="Stop Simulation", width=-1, tag=Tag.STOP_SIMULATION_BUTTON)


def resize() -> None:
    dpg.set_item_width(item=Tag.COMMEND_INPUT, width=dpg.get_item_width(item=Tag.CONSOLE) - Default.RESIZE_OFFSET)
    dpg.set_item_width(item=Tag.NUMBER_OF_SAMPLES, width=dpg.get_item_width(item=Tag.PLOT) - 500)


def set_start_simulation_callback(callback: Callable) -> None:
    dpg.set_item_callback(item=Tag.START_SIMULATION_BUTTON, callback=callback)


def set_stop_simulation_callback(callback: Callable) -> None:
    dpg.set_item_callback(item=Tag.STOP_SIMULATION_BUTTON, callback=callback)


def set_quit_button_callback(callback: Callable) -> None:
    dpg.set_item_callback(item=Tag.QUIT_BUTTON, callback=callback)


def create() -> None:
    _init_theme()
    _init_fonts()
    _header()
    _body()
