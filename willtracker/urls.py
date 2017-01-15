# howdy/urls.py
from django.conf.urls import url
from willtracker import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^Asset Records/$', views.AboutPageView.as_view()),
    url(r'^retrieve records/$', views.RetrieveRecords.as_view()),
    url(r'^view record/$', views.ViewRecord.as_view()),
 ]
