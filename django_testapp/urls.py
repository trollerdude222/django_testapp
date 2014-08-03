from django.conf.urls import patterns, include, url



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^users/', include('my_social_network.urls')),                
    url(r'^admin/', include(admin.site.urls)),
)