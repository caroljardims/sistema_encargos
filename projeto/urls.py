from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'projeto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'saldo.views.index', name='index'),
    url(r'^addprof/', 'saldo.views.addprof', name='addprof'),
    url(r'^addencargo/', 'saldo.views.addencargo', name='addencargo'),
    url(r'^calcularmedia/', 'saldo.views.calcularmedia', name='calcularmedia'),
    url(r'^saldo/', 'saldo.views.saldo', name='saldo'),
    url(r'^versaldo/(?P<anosem>\d+)/$', 'saldo.views.versaldo', name='versaldo'),
]
