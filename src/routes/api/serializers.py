from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from routes.models import Route, Address, Place


class AddressReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'country',
            'street_1',
            'street_2',
            'zip',
            'province',
            'latitude',
            'longitude',
        )


class AddressWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'country',
            'street_1',
            'street_2',
            'zip',
            'province',
            'latitude',
            'longitude',
        )


class PlaceReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            'id', 'name', 'description', 'location'
        )
    location = AddressReadSerializer(required=True)


class PlaceWriteSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Place
        fields = (
            'name', 'description', 'location'
        )
    location = AddressWriteSerializer(required=True)


class RouteReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'name', 'description', 'places', 'user')
    places = PlaceReadSerializer(many=True, required=True)


class RouteWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = (
            'name',
            'description',
            'user',
            'places'
        )
    places = PlaceReadSerializer(many=True, required=True)
