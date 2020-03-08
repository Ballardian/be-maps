from django.shortcuts import get_object_or_404
from drf_rw_serializers import viewsets
from routes.api.serializers import RouteReadSerializer, RouteWriteSerializer, AddressReadSerializer, AddressWriteSerializer, PlaceReadSerializer, PlaceWriteSerializer
from routes import models
from rest_framework import viewsets
from rest_framework.response import Response


class RouteViewSet(viewsets.ModelViewSet):
    queryset = models.Route.objects.all()
    serializer_class = RouteReadSerializer
    read_serializer_class = RouteReadSerializer
    write_serializer_class = RouteWriteSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = AddressReadSerializer
    read_serializer_class = AddressReadSerializer
    write_serializer_class = AddressWriteSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = models.Place.objects.all()
    serializer_class = PlaceReadSerializer
    read_serializer_class = PlaceReadSerializer
    write_serializer_class = PlaceWriteSerializer
