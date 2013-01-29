"""The application's Globals object"""

class Globals(object):

    """Globals acts as a container for objects available throughout the
    life of the application

    """
    ## previous: CDNBASE = "http://c0118811.cdn.cloudfiles.rackspacecloud.com"
    CDNBASE = "http://c118811.r11.cf0.rackcdn.com"
#	c0129431.cdn.cloudfiles.rackspacecloud.com
#    CDNBASE = "http://c97282.r82.cf0.rackcdn.com"

    def __init__(self):
        """One instance of Globals is created during application
        initialization and is available during requests via the
        'app_globals' variable

        """
        pass

