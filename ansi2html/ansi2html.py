#!/usr/bin/python

#Convert ANSI (terminal) colours and attributes to HTML

# Author of original sh script:
#    http://www.pixelbeat.org/docs/terminal_colours/
# Python author:
#    http://github.com/ralphbean/ansi2html/

from genshi.template import TemplateLoader, loader
from genshi import HTML
import subprocess as sp

class Ansi2HTMLConverter(object):
    """ Convert Ansi color codes to CSS+HTML 

    Example:
    >>> conv = Ansi2HTMLConverter()
    >>> ansi = " ".join(sys.stdin.readlines())
    >>> html = conv.convert(ansi)
    """

    def __init__(self, 
                 template='ansi2html.templates.default',
                 dark_bg=True,
                 font_size='normal'):
        self._template = template
        self.dark_bg = dark_bg
        self.font_size = font_size
        self._attrs = None

        from ansi2html import __file__
        self.base = "/".join(__file__.split('/')[:-1])

    def prepare(self, ansi):
        """ Load the contents of 'ansi' into this object """

        # For now, make heavy use of pixelbeat's amazing script.
        cmd = ["%s/ansi2html.sh" % self.base]
        p = sp.Popen(cmd, stdout=sp.PIPE, stdin=sp.PIPE, shell=True)
        body = HTML(p.communicate(ansi)[0], encoding="us-ascii")

        self._attrs = {
            'dark_bg' : self.dark_bg,
            'font_size' : self.font_size,
            'body' : body
        }

        return self._attrs

    def attrs(self):
        """ Prepare attributes for the template """
        if not self._attrs:
            raise Exception, "Method .prepare not yet called."
        return self._attrs

    def template(self):
        """ Load the template """
        toks = self._template.split('.')
        name, path, fname = toks[0], "/".join(toks[1:-1]), toks[-1] + '.html'
        tmpl = TemplateLoader([loader.package(name, path)]).load(fname)
        return tmpl

    def convert(self, ansi):
        return self.template().generate(**self.prepare(ansi)).render('html')
