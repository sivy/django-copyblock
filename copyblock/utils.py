from markdown import markdown
import sys
from django.conf import settings

CACHE = {}

def get_file_contents(filepath):
    fp = open(filepath, 'r')
    content = fp.read()
    fp.close()
    return content

def copydown(filepath, nocache=False, nomarkdown=False):
    if nocache \
       or not settings.COPYBLOCK_CACHE \
       or filepath not in CACHE:
        try:
            content = get_file_contents(filepath)

            if nomarkdown:
                output = content
            else:
                output = markdown(content)
            CACHE[filepath] = output
        except IOError:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            output = '<!-- file %s not found -->' % filepath
    else:
        output = CACHE[filepath]

    return output