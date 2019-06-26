#!/usr/bin/python3
import requests
import sys
import json

API_KEY = "put-vultr-api-key-here"

base_url = "https://api.vultr.com/"

# Get list of instances
headers ={"API-Key": API_KEY}
raw_response = requests.get(base_url+"v1/server/list",headers=headers)
if (raw_response.status_code != 200):
    exit("ERROR:%s"%raw_response.text)

parsed_response = json.loads(raw_response.text)

# Find itself using external ip
ip = requests.get("https://api.ipify.org/").text

servers = list(filter(lambda x: x['main_ip'] == ip, list(parsed_response.values())))
server = servers[0]

SUBID  = server['SUBID']

destory_response = requests.post(base_url+"v1/server/destroy", data=[('SUBID', SUBID)],headers=headers)
print ("Server Destroyed")