try:
    from .alert import AlertHandler
    import AppKit
except Exception as e:
    raise ImportError(e)

class AlertChoca(AlertHandler):
    def execute(self):
        alert = AppKit.NSAlert.alloc().init()
        alert.setMessageText_(self.message)
        AppKit.NSApp.activateIgnoringOtherApps_(True)
        return alert.runModal()

