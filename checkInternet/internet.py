
from urllib import request

def internet_on():
    try:
        response=request.urlopen('http://www.google.com',timeout=1)
        return True
    except request.URLError as err: pass
    return False

