# rpi-picam-monitor
A simple python project to take snapshots from a cam.

## Requirements
In order to use this software:
1. Enable PiCam from raspi-config:
```
$ sudo raspi-config
```

2. Install python3, pip3 and following libraries:
```
$ pip3 install multitimer picamera
```
## Usage

Change settings in settings.json file and execute SystemStarterPM main script to start system:
```
$ python3 SystemStarterPM.py
```
If you use ssh and want to leave it running even without it, install **screen** software with ```$ sudo apt-get install screen```.

Then you can use ```$ screen``` to start a new session and then **ctrl+a**, **d** to exit the screen.

**Remeber** that when you are in a screen and hit **ctrl+c** you will do it inside screen and not killing the screen software.

When you want to **resume** a screen (e.g. when logging to ssh) just do ```$ screen -r```