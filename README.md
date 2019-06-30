# Minecraft server scripts

These are some scripts to turn minecraft servers on and off on vultr and back up the world to dropbox so I don't get a phat bill at the end of the month.

## How it works 
It works by downloading the server from wherever it's hosted and running it.  
When you're done, you run the `backup` and `destroy` commands which backup the world (and other server files) to dropbox and use the vultr api to destroy this server.  
Option to automate shutting down may be coming soon.

## How to use it
To automate the downloading and starting process, you can make a startup script on vultr that clones this repository and runs `./configure` with the options required and then run `./install`