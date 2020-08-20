from django.shortcuts import render
from django.views.generic import DetailView
from .models import Destinations


class DestinationsView(DetailView):
    model = Destinations

    def get_object(self, queryset=None):
        # https://docs.djangoproject.com/en/3.1/ref/models/querysets/
        # https://stackoverflow.com/a/19631233/1439705
        # obj, created = self.model.objects.get_or_create(name='Visite el Teleférico de Mérida')
        # obj, created = self.model.objects.get_or_create(id=1)
        obj = self.model.objects.get(id=1)
        return obj
