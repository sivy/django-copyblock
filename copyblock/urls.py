from django.conf.urls.defaults import *

urlpatterns = patterns('copyblock.views',
    url(r'^$', 'serve', name='serve'),
)
