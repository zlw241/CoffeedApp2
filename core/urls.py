from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
import core.views as coreviews

urlpatterns = patterns('',
  url(r'^$', coreviews.LandingView.as_view()),
  url(r'locations/$', coreviews.LocationListView.as_view()),
  url(r'locations/(?P<pk>\d+)/detail/$', coreviews.LocationDetailView.as_view(), name='location_list'),
  url(r'locations/create/$', login_required(coreviews.LocationCreateView.as_view())),
  url(r'search/$', coreviews.SearchListView.as_view()),
  url(r'locations/(?P<pk>\d+)/update/$', login_required(coreviews.LocationUpdateView.as_view()), name='location_update'),
  url(r'locations/(?P<pk>\d+)/review/create/$', login_required(coreviews.ReviewCreateView.as_view()), name='review_create'),
  url(r'locations/(?P<pk>\d+)/review/update/$', login_required(coreviews.ReviewUpdateView.as_view()), name='review_update'),
  url(r'entrance/$', coreviews.entrance),
)