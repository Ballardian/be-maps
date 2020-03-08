from django.contrib import admin

from .models import Route
from .models import Place
from .models import Address

admin.site.register(Route)
admin.site.register(Place)
admin.site.register(Address)
