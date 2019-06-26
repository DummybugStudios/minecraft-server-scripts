#!/bin/bash

# Stop currently running server
systemctl stop minecraft.service
# Disable it too if you feel like it
systemctl disable minecraft.service

echo Y | apt install zip python3-pip
echo Y | pip3 install dropbox

server_root="/root/minecraft"

server_link="https://server-download-link"

world_link="https://world-download-link"


start="./ServerStart.sh"


# make the folder
mkdir $server_root
cd $server_root

# Download the server
wget $server_link -O server.zip
unzip server.zip
rm server.zip

# Agree to the eula
echo "eula=true" > eula.txt

# Replace the world with your own :O
wget $world_link -O world.zip
unzip -o world.zip
rm world.zip


# TODO: put the backup and destroy exectuable in the correct place

# Start the server
chmod +x "$start"
screen -S server -dm "$start"
