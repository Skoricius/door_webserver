# Webserver app for controlling the relays.

Utils are useful for switching relays on the Raspberry PI. Here, it is designed to turn on and off MOKE instrument, but can be easily adapted to act as a switch for anything else. 
I.e. I also used it to open the garage door with Raspberry PI bridging the switch inside the houes and connected to an internal WIFI network.

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

