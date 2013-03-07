"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
import time
import urllib2

# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password
from routes import url_for


VERSION_FILE = "/home/ed/pylons/dabo/log/latest_version"


def get_current_version():
	with file(VERSION_FILE, "r") as ff:
		return ff.read()


def update_current_version():
	url = "http://daboserver.com/currentversion"
	# Need to wait for the daboserver to update
	time.sleep(30)
	resp = urllib2.urlopen(url)
	with file(VERSION_FILE, "w") as ff:
		ff.write(resp.read())
	return resp
