import os
import stat
from dotenv import dotenv_values
import json

class Config:
    # Paths.
    SRC_BASE = os.path.dirname(__file__)
    FONTS = os.path.join(SRC_BASE, "assets", "fonts")
    STATE_PATH = os.path.join(SRC_BASE, "..", "state.json")
    ASSETS_PATH = os.path.join(SRC_BASE, "assets")

    # Environment variables.
    ENV_VALUES = dotenv_values()

    VIRTUAL_MODE = False

    # Enable virtual mode even if running on Pi.
    VIRTUAL_MODE_OVERRIDE = False

    # Default state values.
    DEFAULTS = {
        "mode": "timed",
        "view": 0
    }

    def initialize_state():
        json_s = None
        if not os.path.isfile(Config.STATE_PATH):
            open(Config.STATE_PATH, "a").close()
            json_s = dict()
        else:
            json_s = Config.read_full()

        os.chmod(Config.STATE_PATH,
            stat.S_IREAD | stat.S_IWRITE |
            stat.S_IRGRP | stat.S_IWGRP |
            stat.S_IROTH
        )            

        if not set(Config.DEFAULTS.keys()).issubset(set(json_s.keys())):
            for key in Config.DEFAULTS.keys():
                if not key in json_s.keys():
                    json_s[key] = Config.DEFAULTS[key]

            Config.update_full(json_s)

    def read_full():
        state = open(Config.STATE_PATH, "r")
        json_s = json.load(state)
        state.close()

        return json_s

    def read_key(key):
        json_s = Config.read_full()
        return json_s[key]

    def update_full(data):
        state = open(Config.STATE_PATH, "w")
        json.dump(data, state)
        state.close()

    def update_key(key, value):
        json_s = Config.read_full()
        json_s[key] = value
        Config.update_full(json_s)
