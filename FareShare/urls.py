
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from offerride.views import index
urlpatterns = [
	url(r'^$',index),
    url(r'^admin/', admin.site.urls),
    url(r'^offerride/', include('offerride.urls')),
    url(r'^signin/', include('signin.urls')),
    ]


#urlpatterns += staticfiles_urlpatterns()
