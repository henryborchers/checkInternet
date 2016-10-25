from .abs_alerters import AbsAlert
try:
    from tkinter import Tk, messagebox
except Exception as e:
    raise ImportError(e)


class TkAlerter(AbsAlert):

    def execute(self):
        window = Tk()
        window.withdraw()
        return messagebox.showerror(title="Internet gone", message=self.message) == "ok"