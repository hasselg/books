import os
import sys
import cherrypy
from cherrypy import wsgiserver

import django.core.handlers.wsgi

class Root(object):
    pass

def main():
    media_root = media_root = os.path.join(os.getcwd(), 'media')
    print "media root: %s" % (media_root)
        
    cherrypy.tree.mount(Root(), '/', config={
        '/media': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': media_root,
        },
    })
    cherrypy.tree.graft(django.core.handlers.wsgi.WSGIHandler(), '/books')


    cherrypy.engine.start()
    