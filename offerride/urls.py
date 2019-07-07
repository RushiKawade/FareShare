from django.conf.urls import url
from . import views

app_name = 'offerride'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^rides/$', views.rides, name='rides'),
    url(r'^addride/$', views.addride, name='addride'),
    url(r'^submitride/$', views.submitride, name='submitride'),
    url(r'^join/$', views.join, name='join'),
    url(r'^addcar/$', views.addcar, name='addcar'),
    url(r'^submitcar/$', views.submitcar, name='submitcar'),

    
]