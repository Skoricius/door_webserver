# Webserver app for controlling the relays.

Utils are useful for starting and stopping MOKE.

Run app.py to start the server, run connection_checker.py to constantly check the connection to the internet and local computer.
Run `bash start_moke_listeners.sh` to start both.

Edited the shell configuration to have start and stop aliases for starting and stopping MOKE.


## Setting up the autostart:
Option 3 in: https://www.itechfy.com/tech/auto-run-python-program-on-raspberry-pi-startup/
```
mkdir /home/pi/.config/autostart
vi /home/pi/.config/autostart/PiCube.desktop    
```
In the file, write:
```
[Desktop Entry]
Type= Application
Name= MokeSafe
Exec= bash /home/pi/Desktop/webserver/start_moke_listeners.sh
```

