from django.shortcuts import render
from django.views.generic import TemplateView

class PlaceholderHome(TemplateView):
    template_name = "supportdesk/placeholder.html"