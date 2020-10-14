from utils.check_connection import check_computer_on, check_internet_up
from utils.set_state import stop_moke
import time

time_interval = 5

while True:
    time.sleep(time_interval)
    if not (check_computer_on() and check_internet_up()):
        stop_moke()
