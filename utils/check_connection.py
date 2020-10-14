import os
from urllib import request


def check_computer_on(ip_address='130.209.204.102'):
    response = os.system("ping -c 1 " + ip_address)

    # and then check the response...
    if response == 0:
        return True
    else:
        return False


def check_internet_up(host="http://google.com"):
    try:
        request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


if __name__ == "__main__":
    print(check_computer_on())
    print(check_internet_up())
