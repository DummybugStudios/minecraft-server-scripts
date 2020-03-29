import json
import os

# Get the path relative to the current directory
basedir = os.path.dirname(__file__)

config_file = os.path.join(basedir, "config.json")
temp_config = os.path.join(basedir, "tempconfig.json")

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
    with open(temp_config, "w") as f:
        f.write ( json.dumps(new_config, indent=4) )

def load_temp_config():
    with open(temp_config, "r") as f:
        raw = f.read()
        return (json.loads(raw))
