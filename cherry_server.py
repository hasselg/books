import os
import sys
import cherrypy
from cherrypy import wsgiserver

import django.core.handlers.wsgi

class Root(object):
    pass

class Server(object):
    def __init__(self):
        cherrypy.log.screen = False
        media_root = media_root = os.path.join(os.getcwd(), 'media')
        # print "media root: %s" % (media_root)
        
        cherrypy.tree.mount(Root(), '/', config={
            '/media': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': media_root,
            },
        })
        cherrypy.tree.graft(django.core.handlers.wsgi.WSGIHandler(), '/books')

    def start(self, block=False):
        cherrypy.engine.start()
        if block:
            try:
                cherrypy.engine.block()
            except KeyboardInterrupt:
                cherrypy.engine.stop()

    def stop(self):
        cherrypy.engine.exit()
