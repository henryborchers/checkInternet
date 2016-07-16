from unittest import TestCase

from checkInternet.Alerts.CocoAlert import AlertChoca
from checkInternet.Alerts.tkAlert import AlertTK


class TestAlertTK(TestCase):
    def setUp(self):
        self.t = AlertTK("internet is down")

    def test_execute(self):
        self.assertEqual(self.t.execute(), True)


class TestAlertOSX(TestCase):
    def setUp(self):
        self.t = AlertChoca("internet is down")

    def test_execute(self):
        self.assertEqual(self.t.execute(), True)