from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index_page, name='index'),
	url(r'^list/',views.list_page,name='list'),

]
