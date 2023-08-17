from django.contrib import admin
from .models import RaspberryShakeStations, RaspberryShakeQuakes
# Register your models here.
admin.site.register(RaspberryShakeStations)
admin.site.register(RaspberryShakeQuakes)