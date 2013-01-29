import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from dabo.lib.base import BaseController, render
import dabo.lib.helpers as h

log = logging.getLogger(__name__)

class LatestController(BaseController):
    def index(self):
		h.update_current_version()
		return "OK"
		
