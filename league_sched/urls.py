from django.conf.urls import url
from league_sched import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^league_names/(?P<pk>[0-9]+)/$', views.LeagueNameDetail.as_view()),
]
