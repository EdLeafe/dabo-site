import logging
import os
import re
import urllib2

from pylons import request, response, session, tmpl_context as c
from pylons import app_globals
from pylons.controllers.util import abort, redirect

from dabo.lib.base import BaseController, render

log = logging.getLogger(__name__)
dl_pat = re.compile(r"dabo_(.{3})_download")


def get_current_version():
	url = "http://daboserver.com/currentversion"
	resp = urllib2.urlopen(url)
	return resp.read()


class GrabitController(BaseController):
	def index(self, url):
		try:
			dl_platform = dl_pat.match(url).groups()[0]
		except AttributeError:
			dl_platform = None
		if dl_platform:
			ext = {"nix": "tar.gz", "win": "zip"}[dl_platform]
			try:
				version = get_current_version()
			except Exception as e:
				log.error("Error getting version info: %s" % e)
				return "<h2>Sorry, something didn't work as expected. Please send a nasty email " \
						"expressing your anger to <a href='mailto:ed@leafe.com'>the incompetent guy</a> " \
						"who runs this site.i</h2>"
			pth = "https://github.com/dabodev/dabo/archive/%s.%s" % (version, ext)
		else:
			pth = str(os.path.join(app_globals.CDNBASE, url))
		addr = request.remote_addr
		log.info("[%s] Download Request: %s" % (addr, url))
		redirect(pth)
