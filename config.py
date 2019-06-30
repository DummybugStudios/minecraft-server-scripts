#!/usr/bin/python3
import json


config_file = "config.json"
def load_config():

    config_raw = open (config_file, "r").read()
    config = json.loads(config_raw)

    return config

def save_config(new_config):
    config_string = json.dumps(new_config)
    f = open(config_file, "w")
    f.write(config_string)
    f.close()