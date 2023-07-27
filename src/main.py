import dearpygui.dearpygui as dpg
from view import layout
import tomllib
from src.model.app import MainApp


def load_config() -> str:
    with open("config/config.toml", "rb") as config_file:
        config_data = tomllib.load(config_file)
        return f"{config_data['name']} {config_data['version']}"


def quit_app() -> None:
    MainApp.stop_threads()
    dpg.destroy_context()
    # MainApp.main_worker.stop_working()  # stop working thread
    # MainApp.plotting_worker.stop_plotting()
    # MainApp.main_worker.worker_thread.join()
    # MainApp.plotting_worker.plotting_thread.join()


def main() -> None:
    dpg.create_context()
    layout.create()  # create layout
    """"
        It is important to create layout before starting working thread
        because thread may want to use some object from layout before it's creation
    """

    # layout.set_start_button_callback(app.start_button_callback)
    # layout.set_stop_button_callback(app.stop_button_callback)

    layout.set_start_simulation_callback(MainApp.start_threads)
    layout.set_stop_simulation_callback(MainApp.stop_threads)
    layout.set_quit_button_callback(quit_app)

    dpg.create_viewport(title=load_config())
    dpg.set_viewport_resize_callback(layout.resize)
    dpg.configure_app(**layout.Config.APP_CONFIG)
    dpg.setup_dearpygui()
    layout.resize()
    dpg.show_viewport()
    dpg.maximize_viewport()  # Optional
    # MainApp.start_threads() # start working thread

    dpg.start_dearpygui()
    MainApp.stop_threads()
    dpg.destroy_context()


if __name__ == '__main__':
    main()
