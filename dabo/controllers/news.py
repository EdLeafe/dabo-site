#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from pylons import request, response, session
from pylons import tmpl_context as c
from pylons.controllers.util import abort, redirect
from pylons.templating import render_mako as render

from dabo.lib.base import BaseController, render
#import dabo.model as model

log = logging.getLogger(__name__)

class NewsController(BaseController):

    def index(self):
        raw_content = file("/home/ed/pylons/dabo/dabo/templates/news_content.html").read()
        c.news_content = raw_content.decode("utf-8")
        return render("/news.html")
