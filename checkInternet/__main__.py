from time import sleep
from tkinter import messagebox, Tk
import sys
import datetime
from checkInternet.Alerts import alert
from checkInternet import internet
# from internet import internet_fail, internet_on
# import Alerts
# import internet
import argparse


def reporter(f):

    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return x

    return wrap


@reporter
def report_internet():
    x = internet.multi_attempt()
    if x:
        print("[{}] Internet up. Press \"Ctrl + c\" to quit".format(str(datetime.datetime.now().isoformat())))
    return x


def check_internet(fail_callback, sleeptime=60):
    try:
        while report_internet():
            sleep(sleeptime)
        sys.stdout.write('\a')
        sys.stdout.flush()
        fail_callback("internet Down at {}".format(str(datetime.datetime.now().isoformat())))
    except KeyboardInterrupt:
        print()
        print("Exiting")
        pass



def main():
    parser = argparse.ArgumentParser(description="Checks to see to let you know if the internet is still accessible")
    parser.add_argument("frequency", nargs="?", type=int, default=60,
                        help="How many seconds between each check. (Default is 60)")
    args = parser.parse_args()
    print()
    print("Starting to monitor Internet access\n")
    print("Checking every {} second(s)".format(args.frequency))
    check_internet(alert.Alert, args.frequency)
    # check_internet(no_internet_tk, args.frequency)
    print("Goodbye")

if __name__ == '__main__':
    main()