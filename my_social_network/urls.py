from django.conf.urls import patterns, url

from my_social_network import views

urlpatterns = patterns('',
    url(r'^$', views.viewusers, name='allusers')
    url(r'^(?P<username>\d+)/friends/$', views.viewfriends, name='friends') 
    url(r'^(?P<username>\d+)/followers/$', views.viewfollowers, name='followers')      
    url(r'^(?P<username>\d+)/following/$', views.viewfollowing, name='following')      
 
) 