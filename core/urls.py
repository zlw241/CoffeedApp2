from django.conf.urls import patterns, include, url
import core.views as coreviews

urlpatterns = patterns('',
  url(r'^$', coreviews.LandingView.as_view()),
  url(r'locations/$', coreviews.LocationListView.as_view()),
  url(r'locations/(?P<pk>\d+)/detail/$', coreviews.LocationDetailView.as_view(), name='location_list'),
  url(r'locations/create/$', coreviews.LocationCreateView.as_view()),
  url(r'search/$', coreviews.SearchListView.as_view()),
  url(r'locations/(?P<pk>\d+)/update/$', coreviews.LocationUpdateView.as_view(), name='location_update'),
  url(r'locations/(?P<pk>\d+)/review/create/$', coreviews.ReviewCreateView.as_view(), name='review_create'),
  url(r'locations/(?P<pk>\d+)/review/update/$', coreviews.ReviewUpdateView.as_view(), name='review_update'),
)