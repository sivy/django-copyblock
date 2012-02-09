from django.conf import settings
import os
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from copyblock.utils import copydown

def serve(request, path):
    # files should be here
    root = settings.COPYBLOCK_ROOT
    template = ''
    try:
        template = settings.COPYBLOCK_TEMPLATE
    except AttributeError, ae:
        HttpResponseServerError('Template not defined.')

    print template
    
    filepath = "%s/%s.markdown" % (root, path)
    print filepath

    # check file path
    if not os.path.exists(filepath):
        return HttpResponseNotFound()

    # run through markdown?
    output = copydown(filepath, nocache=nocache, nomarkdown=nomarkdown)
    print output

    # run as template? which first?
    return render_to_response(template, {
        'output': output,
    }, context_instance=RequestContext(request))