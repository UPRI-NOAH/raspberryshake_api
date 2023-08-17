from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response

# Import modules for models, serializers, filters
from api.stations.models import RaspberryShakeStations, RaspberryShakeQuakes
from api.stations.serializer import RaspberryShakeStationsSerializer, RaspberryShakeQuakesSerializer
from api.stations.filters import RaspberryShakeStationsFilter, RaspberryShakeQuakesFilter

from django.core.serializers import serialize
from django_filters import rest_framework as filters

import json
from api.stations import stations, quakes
# Create your views here.

class RaspberryShakeStationsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = RaspberryShakeStations.objects.all().order_by('code')
    serializer_class = RaspberryShakeStationsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RaspberryShakeStationsFilter

    def list(self, request):
        # stations.fetch_stations()
        queryset = self.get_queryset()
        queryset = self.filterset_class(self.request.GET, queryset=queryset)
        data = serialize('geojson', queryset.qs)
        return Response(data = json.loads(data))

class RaspberryShakeQuakesViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = RaspberryShakeQuakes.objects.all().order_by('code')
    serializer_class = RaspberryShakeQuakesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RaspberryShakeQuakesFilter

    def list(self, request):
        # quakes.fetch_quakes()
        queryset = self.get_queryset()
        queryset = self.filterset_class(self.request.GET, queryset=queryset)
        data = serialize('geojson', queryset.qs)
        return Response(data = json.loads(data))
