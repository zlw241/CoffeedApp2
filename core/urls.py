from django.conf.urls import patterns, include, url
import core.views as coreviews

urlpatterns = patterns('',

  url(r'^$', coreviews.LandingView.as_view()),
  url(r'locations/$', coreviews.LocationListView.as_view()),
  url(r'locations/(?P<pk>\d+)/detail/$', coreviews.LocationDetailView.as_view(), name='location_list'),
)