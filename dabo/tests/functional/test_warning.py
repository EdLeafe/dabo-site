from dabo.tests import *

class TestWarningController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='warning', action='index'))
        # Test response...
