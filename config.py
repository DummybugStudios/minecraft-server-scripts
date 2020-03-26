import json
import os

basedir = os.path.dirname(__file__)

config_file = os.path.join(basedir, "config.json")
def load_config():

    config_raw = open (config_file, "r").read()
    config = json.loads(config_raw)

    return config

def save_config(new_config):
    config_string = json.dumps(new_config, indent=4)
    f = open(config_file, "w")
    f.write(config_string)
    f.close()


def save_temp_config(new_config):
    pass

def load_temp_config():
    pass