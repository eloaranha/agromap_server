from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import tech.views

# Examples:
# url(r'^$', 'websrv_tech.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    # url(r'^$', hello.views.index, name='index'),
    url(r'^db', tech.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('tech.urls')),
]
