from django.conf.urls import url
from league_sched import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^league_names/(?P<pk>[0-9]+)/$', views.LeagueNameDetail.as_view()),
    url(r'^teams/(?P<pk>[0-9]+)/$', views.TeamDetail.as_view()),
    url(r'^team_members/(?P<pk>[0-9]+)/$', views.TeamMemberDetail.as_view()),
    url(r'^future_matches/(?P<pk>[0-9]+)/$', views.FutureMatchDetail.as_view()),
    url(r'^available_times/(?P<pk>[0-9]+)/$', views.AvailableTimeDetail.as_view()),
    url(r'^completed_matches/(?P<pk>[0-9]+)/$', views.CompletedMatchDetail.as_view()),
]
