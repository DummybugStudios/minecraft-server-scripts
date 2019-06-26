#!/usr/bin/python3

import os

import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError



#TODO: make a mechanism to configure all this for future scripts

basepath = "/root/minecraft"
filenames = ["world", "server.properties", "ops.json"]
zipname  = "world.zip"

TOKEN = "put-dropbox-token-here"


def backup(local, remote):
    f = open(local, 'rb');

    try:
        dbx.files_upload(f.read(), remote, mode=WriteMode('overwrite'))
    except ApiError as err:
        print (err.user_message_text)

dbx = dropbox.Dropbox(TOKEN)
try:
    dbx.users_get_current_account()
except AuthError as err:
    exit("Invalid token")


# compress world
os.chdir(basepath)

cmd = "zip -r %s "%zipname
for filename in filenames:
    cmd += " " + filename
os.system(cmd);
backup(zipname, "/"+zipname)