from django.conf import settings
from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Address(models.Model):
    street_1 = models.CharField(max_length=500, null=True, blank=True)
    street_2 = models.CharField(max_length=500, null=True, blank=True)
    zip = models.CharField(max_length=20, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=30, null=True, blank=True, decimal_places=20)
    longitude = models.DecimalField(
        max_digits=30, null=True, blank=True, decimal_places=20)


class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)
    route = models.ForeignKey(
        Route,
        related_name="places",
        on_delete=models.CASCADE,
    )
