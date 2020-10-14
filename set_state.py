import RPi.GPIO as GPIO
import sys

state = int(sys.argv[1])
print(state)

port = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.OUT)
if state == 1:
    print('setting high')
    GPIO.output(port, GPIO.HIGH)
elif state == 0:
    print('setting low')
    GPIO.output(port, GPIO.LOW)
