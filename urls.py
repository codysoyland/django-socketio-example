import os
from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'chat.html'}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': os.path.join(settings.BASE_PATH, 'media')}),
)

urlpatterns += patterns('views',
    (r'^socket\.io', 'socketio'),
)
