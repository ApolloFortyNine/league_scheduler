from django.conf.urls import url
from league_sched import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^league_names/(?P<pk>[0-9]+)/$', views.league_name_detail),
]
