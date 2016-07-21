from django.conf.urls import url
from league_sched import views

urlpatterns = [
    url(r'^users/$', views.user_list),
]
