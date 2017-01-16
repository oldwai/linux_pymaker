from django.conf.urls import patterns, include, url
from django.contrib import admin
from compare_testweb.view import hello
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compare_testweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^$', hello),
    url(r'^admin/', include(admin.site.urls)),
)
