from config.default import Default


class Config:
    WINDOW_CONFIG = dict(no_collapse=True, no_close=True)
    APP_CONFIG = dict(docking=True, docking_space=True, init_file=Default.INIT_FILE_PATH, load_init_file=True)
