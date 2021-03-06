from abc import ABCMeta, abstractmethod
import sys


class AlertHandler(metaclass=ABCMeta):
    def __init__(self, message):
        self.message = message
        self.clicked = self.execute()

    @abstractmethod
    def execute(self):
        pass


def Alert(message):
    if sys.platform == "darwin":
        try:
            return _alert_factory(message=message, engine="cocoa")

        except ImportError:
            print("Unable to use cocoa.", file=sys.stderr)
            pass

    return _alert_factory(message=message)
    pass

def _alert_factory(message, engine="tk"):
    try:
        if engine == "tk":
            from .tkAlert import AlertTK
            return AlertTK(message)
        if engine == "cocoa":
            from .CocoAlert import AlertCoca
            return AlertCoca(message)
        else:
            raise AttributeError("{} is an invalid error engine".format(engine))
    except ImportError as e:
        raise ImportError("Engine unavailable: {}".format(e))

# class AlertOSX(AlertHandler):
#     def execute(self):
#         pass