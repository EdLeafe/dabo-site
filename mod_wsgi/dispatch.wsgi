# Add the virtual Python environment site-packages directory to the path
#import site
#site.addsitedir('/home/ed/projects/dabo/env/lib/python2.5/site-packages')

# Avoid ``[Errno 13] Permission denied: '/var/www/.python-eggs'`` messages
import os
os.environ['PYTHON_EGG_CACHE'] = '/home/ed/projects/dabo/egg-cache'

# Load the Pylons application
from paste.deploy import loadapp
#application = loadapp('config:/home/ed/projects/dabo/production.ini')
# From the suggestion of Nathen Hinson, to fix the empty logging issue
from paste.script.util.logging_config import fileConfig
INIFILE = "/home/ed/projects/dabo/production.ini"
fileConfig(INIFILE)
application = loadapp("config:%s" % INIFILE)
