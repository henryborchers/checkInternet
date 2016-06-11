from time import sleep
from tkinter import messagebox
import sys
import datetime
from .internet import internet_on


def main():
    print("Hello")
    while internet_on():
        print("[{}] Internet up".format(str(datetime.datetime.now().isoformat())))
        sleep(60)
    sys.stdout.write('\a')
    sys.stdout.flush()
    messagebox.showerror(title="Internet gone", message="[{}] \nInternet down".format(str(datetime.datetime.now().isoformat())))


if __name__ == '__main__':
    main()