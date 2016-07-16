
from urllib import request

import time


def internet_on(timeout=2):
    try:
        response = request.urlopen('http://www.google.com', timeout=timeout)
        return True
    except request.URLError as err: pass
    return False

def internet_fail():
    return False


def multi_attempt(trys=3, timeout=2):
    for _ in range(trys):
        if internet_on(timeout=timeout):
            return True
        else:
            time.sleep(10)
            continue

    return False
