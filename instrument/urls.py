from django.conf.urls import patterns, url
from instrument import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^login/', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^dayShow/(?P<number_of_year>[\w\-]+)/(?P<number_of_month>[\w\-]+)/(?P<number_of_day>[\w\-]+)/$', views.dayShow, name='dayShow'),
)
	