from time import sleep
from tkinter import messagebox
import sys
import datetime
from internet import internet_on
import argparse


def reporter(f):

    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return x

    return wrap


@reporter
def report_internet():
    x = internet_on()
    if x:
        print("[{}] Internet up. Press \"Ctrl + c\" to quit".format(str(datetime.datetime.now().isoformat())))
    return x


def check_internet(sleeptime=60):
    try:
        while report_internet():
            sleep(sleeptime)
        sys.stdout.write('\a')
        sys.stdout.flush()
        messagebox.showerror(title="Internet gone", message="[{}] \nInternet down".format(str(datetime.datetime.now().isoformat())))
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
    check_internet(args.frequency)
    print("Goodbye")

if __name__ == '__main__':
    main()