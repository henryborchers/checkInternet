from .abs_alerters import AbsAlert
try:
    import AppKit
except Exception as e:
    raise ImportError


class CocoAlerter(AbsAlert):

    def execute(self):
        alert = AppKit.NSAlert.alloc().init()
        alert.setMessageText_(self.message)
        AppKit.NSApp.activateIgnoringOtherApps_(True)
        return alert.runModal()

