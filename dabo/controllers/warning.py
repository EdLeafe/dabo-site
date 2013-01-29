import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect

from dabo.lib.base import BaseController, render

log = logging.getLogger(__name__)

class WarningController(BaseController):
    def index(self):
        # Return a rendered template
        #return render('/warning.mako')
        # or, return a response
        return 'Hello World'


    def simplecrypt(self):
        return """WARNING: <br />
Your application uses SimpleCrypt, which is fine for testing but should<br />
not be used in production, because:<br />
<br />
1) Anyone with a copy of Dabo could decrypt your password.<br />
<br />
2) It isn't portable between 32-bit and 64-bit python. See the trac<br />
   ticket at http://trac.dabodev.com/ticket/1179 for more information.<br />
"""