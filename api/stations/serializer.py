from rest_framework import serializers
from api.stations.models import RaspberryShakeStations, RaspberryShakeQuakes

class RaspberryShakeStationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaspberryShakeStations
        fields = [
            "code",
            "elev",
            "online",
            "acc",
            "vel",
            "disp",
            "timestamp",
            "address",
            "loc_pnt",
        ]

class RaspberryShakeQuakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaspberryShakeQuakes
        fields = [
            "code",
            "depth",
            "mag",
            "timestamp",
            "agency",
            "location",
            "loc_pnt",
        ]
