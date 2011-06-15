from docutils import core
from docutils.core import publish_string
import cherrypy
from mako.template import Template

class Render(object):
    def index(self, text='Hello, world!\n================='):
        parts = core.publish_parts(
                                   source=text,
                                   writer_name='html')
        
        return Template("hello ${data}!").render(data="world") + parts['body_pre_docinfo']+parts['fragment']
    index.exposed = True
