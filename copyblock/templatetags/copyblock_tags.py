from django import template
from django.template.base import Node, NodeList, Template, Context, Variable
from django.template.base import TemplateSyntaxError, VariableDoesNotExist, BLOCK_TAG_START, BLOCK_TAG_END, VARIABLE_TAG_START, VARIABLE_TAG_END, SINGLE_BRACE_START, SINGLE_BRACE_END, COMMENT_TAG_START, COMMENT_TAG_END
from markdown import markdownFromFile, markdown
from django.conf import settings

from copyblock.utils import copydown

register = template.Library()

CACHE = {}

class CopyBlockNode(Node):
    def __init__(self, filepath, nocache, nomarkdown):
        self.filepath = filepath
        self.nocache = nocache
        self.nomarkdown = nomarkdown

    def render(self, context):
        filepath = "%s/%s.markdown" % (settings.COPYBLOCK_ROOT, self.filepath)
        nocache = self.nocache
        nomarkdown = self.nomarkdown
        
#        if nocache \
#           or not settings.COPYBLOCK_CACHE \
#           or filepath not in CACHE:
#            try:
#                content = get_file_contents(filepath)
#
#                if nomarkdown:
#                    output = content
#                else:
#                    output = markdown(content)
#                CACHE[self.filepath] = output
#            except IOError:
#                import sys
#                exc_type, exc_value, exc_traceback = sys.exc_info()
#                output = '<!-- file %s not found -->' % filepath
#        else:
#            output = CACHE[self.filepath]

        output = copydown(filepath, nocache=nocache, nomarkdown=nomarkdown)

        return output

def copyblock(parser, token):
    """
    Outputs the contents of a given copy file into the page.

    Like a simple "include" tag, the ``copyblock`` tag includes the contents
    of another file -- which must exist under settings.COPYBLOCK_ROOT --
    in the current page, after running it through markdown::

        {% copyblock welcome_message %}

        {% copyblock help/how_to_use %}

    If the optional "nocache" parameter is given, the copyblock cache will not be consulted,
    otherwise, the file output will be read from the cache to save disk IO. Processed file
    output is cached while the app is running.

        {% copyblock welcome nocache %}
        
    If the content should not be processed as markdown, the "nomarkdown" parameter can be
    passed to the tag:

        {% copyblock welcome nomarkdown %}
    
    """
    args = token.contents.split()
    nocache = False
    nomarkdown = False

    if 'nocache' in args:
        nocache=True
    if 'nomarkdown' in args:
        nomarkdown=True

    return CopyBlockNode(args[1], nocache, nomarkdown)

copyblock = register.tag(copyblock)
