import RPi.GPIO as GPIO
import sys

PORT = 15


def start_moke():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PORT, GPIO.OUT)
    GPIO.output(PORT, GPIO.LOW)


def stop_moke():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(PORT, GPIO.HIGH)


if __name__ == "__main__":
    state = int(sys.argv[1])
    if state == 1:
        start_moke()
        print('Started')
    elif state == 0:
        stop_moke()
        print('Stopped')
