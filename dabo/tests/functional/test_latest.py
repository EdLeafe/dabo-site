from dabo.tests import *

class TestLatestController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='latest', action='index'))
        # Test response...
