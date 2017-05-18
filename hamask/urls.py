from django.conf.urls import url

from . import views

app_name = 'hamask'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/', views.index, name='index'),
	url(r'^programs/(?P<pk>[0-9]+)', views.programs, name='programs'),
	url(r'^programs/', views.programs, name='programs'),
	url(r'^logs/', views.logs, name='logs'),
	url(r'^stats/', views.stats, name='stats'),
]