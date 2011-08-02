from django.conf import settings
import os
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError

def serve(request, path):
    # files should be here
    root = settings.COPY_BLOCK_ROOT
    # check file path
    if not os.path.exists("%s/%s" % (root, path)):
        return HttpResponseNotFound()

    # run through markdown?
    
    # run as template? which first?