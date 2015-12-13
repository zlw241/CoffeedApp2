from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import core.models as coremodels

class LandingView(TemplateView):
	template_name = "base/index.html"

class LocationListView(ListView):
    model = coremodels.Locations
    template_name = "locations/list.html"


class LocationDetailView(DetailView):
    model = coremodels.Locations
    template_name = "locations/detail.html"
    context_object_name = 'location'