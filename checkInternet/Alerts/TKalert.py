try:
    from Alerts.alert import AlertHandler
    from tkinter import Tk, messagebox
except Exception as e:
    raise ImportError(e)

class AlertTK(AlertHandler):
    def execute(self):
        window = Tk()
        window.withdraw()
        return messagebox.showerror(title="Internet gone", message=self.message) == "ok"