from django.conf import settings



def is_copyblock_file(filename):
    dir = settings.COPY_BLOCK_ROOT
    if open("%s/%s" % (dir, filename), 'r'):
        return True