from dabo.tests import *

class TestGrabitController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='grabit', action='index'))
        # Test response...
