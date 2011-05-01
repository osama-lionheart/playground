import sys
sys.stdout = sys.stderr

import atexit
import threading
import cherrypy

cherrypy.config.update({'environment': 'embedded', 'tools.caching.on': False})

if cherrypy.__version__.startswith('3.0') and cherrypy.engine.state == 0:
    cherrypy.engine.start(blocking=False)
    atexit.register(cherrypy.engine.stop)

#application = cherrypy.Application(root, script_name=None, config=None)

#==============================================================================
'''
Import all the necessary controller module for the mapping.
'''
import os
sys.path.append(os.path.dirname(__file__))

import root, render

cherrypy.tree.mount(root.Root(), '/')
cherrypy.tree.mount(render.Render(), '/render')

application = cherrypy.tree
