from django.conf.urls import url

from . import views

app_name = 'alumniLinkedin'

urlpatterns = [

    # Homepage
    url(r'^$', views.index, name='index'),

    # Reader
    url(r'^reader/$', views.reader, name='reader'),

    # API call
    url(r'^api/$', views.call_api, name='api'),

]