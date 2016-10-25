from inspect import getmembers, isclass, isabstract
from . import Alerts

class AlertFactory:
    _alerts = {}

    def __init__(self):
        self.load_alerts()

    def load_alerts(self):
        classes = getmembers(Alerts, lambda m: isclass(m) and not isabstract(m))

        for name, _type in classes:
            if isclass(_type) and issubclass(_type, Alerts.AbsAlert):
                self._alerts.update([[name, _type]])

    def create_alerter(self, alert_type: Alerts.AlertTypes)->Alerts.AbsAlert:
        if isinstance(alert_type, Alerts.AlertTypes):
            alert_type = alert_type.value
        if alert_type in self._alerts:
            return self._alerts[alert_type]()
        else:
            raise ValueError("{} is not a valid alert type for your current machine.".format(alert_type))