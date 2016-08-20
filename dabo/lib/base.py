"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController
from pylons import request, response, session
from pylons import tmpl_context as c
from pylons.templating import render_mako as render

class BaseController(WSGIController):
    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        c.http_host = request.environ["HTTP_HOST"]
        return WSGIController.__call__(self, environ, start_response)
