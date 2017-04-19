from django.conf.urls import url

from . import views
urlpatterns = [
       url(r'^$', views.index, name='index'),
       url(r'^step1/$', views.step1, name='step1'),
       url(r'^step2/$', views.step2, name='step2'),
       url(r'^step3/$', views.step3, name='step3'),
#       url(r'^step4/$', views.step4, name='step4'),
]