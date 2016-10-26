from django.conf.urls import patterns, url 
from tutorial_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
	url(r'^categories/(Category_name_slug>[w-]+)/$', views.category, name='category'),
	)