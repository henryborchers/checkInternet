from unittest import TestCase

import sys


class TestSanity(TestCase):
    def test_Sanity(self):
        pass

class TestDependencies(TestCase):
    if sys.platform == "darwin":
        def test_apple(self):
            import AppKit
            from AppKit import NSAlert