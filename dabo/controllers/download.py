import logging

from pylons import request, response, session
from pylons import tmpl_context as c
from pylons.controllers.util import abort, redirect
from pylons.templating import render_mako as render

from dabo.lib.base import BaseController, render
#import dabo.model as model

log = logging.getLogger(__name__)


class DownloadController(BaseController):

    def index(self):
        return render("/download.html")
