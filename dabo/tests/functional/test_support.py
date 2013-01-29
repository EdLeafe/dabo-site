from dabo.tests import *

class TestSupportController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='support', action='index'))
        # Test response...
