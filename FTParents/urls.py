from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import RedirectView
admin.autodiscover()

urlpatterns = patterns('',
    # Core:
    url(r'^$', 'app.views.landing', name ='landing'),
    url(r'^Embarazo/$', 'app.views.Embarazo', name ='Section'),
    url(r'^E1/$', 'app.views.E1', name ='detail'),
    url(r'^E2/$', 'app.views.E2', name ='detail'),
    url(r'^E3/$', 'app.views.E3', name ='detail'),
    url(r'^E4/$', 'app.views.E4', name ='detail'),
    url(r'^Nutricion/$', 'app.views.Nutricion', name ='Section'),
    url(r'^N1/$', 'app.views.N1', name ='detail'),
    url(r'^N2/$', 'app.views.N2', name ='detail'),
    url(r'^Papa/$', 'app.views.Papa', name ='Section'),
    url(r'^PP1/$', 'app.views.PP1', name ='detail'),
    url(r'^PP2/$', 'app.views.PP2', name ='detail'),
    url(r'^CuidadosHigiene/$', 'app.views.Cuidados', name ='Section'),
    url(r'^CH1/$', 'app.views.CH1', name ='detail'),
    url(r'^CH2/$', 'app.views.CH2', name ='detail'),
    url(r'^Vestimenta/$', 'app.views.Vestimenta', name ='Section'),
    url(r'^V1/$', 'app.views.V1', name ='detail'),
    url(r'^Juegos/$', 'app.views.Juegos', name ='Section'),
    url(r'^G1/$', 'app.views.G1', name ='detail'),
    url(r'^G2/$', 'app.views.G2', name ='detail'),
    url(r'^G3/$', 'app.views.G3', name ='detail'),
    url(r'^apps/$', 'app.views.apps', name ='detail'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    #url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )