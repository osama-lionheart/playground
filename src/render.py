from docutils.core import publish_string
import cherrypy

class Render(object):
    def index(self, text='Hello, world!\n================='):
        return publish_string(
                              source=text,
                              settings_overrides={'file_insertion_enabled': 0, 'raw_enabled': 0},
                              writer_name='html')
    index.exposed = True
