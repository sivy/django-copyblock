from django import template
from django.template.base import Node, NodeList, Template, Context, Variable
from django.template.base import TemplateSyntaxError, VariableDoesNotExist, BLOCK_TAG_START, BLOCK_TAG_END, VARIABLE_TAG_START, VARIABLE_TAG_END, SINGLE_BRACE_START, SINGLE_BRACE_END, COMMENT_TAG_START, COMMENT_TAG_END
from markdown import markdownFromFile, markdown
from django.conf import settings

register = template.Library()

copy_cache = {}

class CopyBlockNode(Node):
    def __init__(self, filepath, nocache):
        print "copyblock node %s %s" % (filepath, nocache)
        self.filepath = filepath
        self.nocache = nocache

    def render(self, context):
        filepath = "%s/%s.markdown" % (settings.COPY_BLOCK_ROOT, self.filepath)
        nocache = self.nocache
        
        if nocache or filepath not in copy_cache:
            try:
                fp = open(filepath, 'r')
                content = fp.read()
                fp.close()

                output = markdown(content)
                copy_cache[self.filepath] = output
            except IOError, e:
                import sys
                exc_type, exc_value, exc_traceback = sys.exc_info()
                output = '<!-- file %s not found -->' % filepath
        else:
            output = copy_cache[self.filepath]
        
        return output

def copyblock(parser, token):
    """
    Outputs the contents of a given copy file into the page.

    Like a simple "include" tag, the ``copyblock`` tag includes the contents
    of another file -- which must exist under settings.COPY_BLOCK_ROOT --
    in the current page, after running it through markdown::

        {% copyblock welcome_message nocache=True %}

        {% copyblock help/how_to_use %}

    If the optional "nocache" parameter is given, the copyblock cache will not be consulted,
    otherwise, an included and processed file will be cached while the app is running.
    
    """
    bits = token.contents.split()
    nocache = False
    if len(bits) not in (2, 3):
        raise TemplateSyntaxError("'ssi' tag takes one argument: the path to"
                                  " the file to be included")
    if len(bits) == 3:
        if bits[2] == 'nocache':
            nocache = True
        else:
            raise TemplateSyntaxError("Second (optional) argument to %s tag"
                                      " must be 'parsed'" % bits[0])
    return CopyBlockNode(bits[1], nocache)
copyblock = register.tag(copyblock)
