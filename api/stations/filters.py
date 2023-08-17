import django_filters

from api.stations.models import RaspberryShakeStations, RaspberryShakeQuakes

class RaspberryShakeStationsFilter(django_filters.FilterSet):
    # online = django_filters.BooleanFilter(field_name="online")
    class Meta:
        model = RaspberryShakeStations
        fields = {
            'code': ['exact'],
            'online': ['exact'],
            'elev':[
                'exact',
                'gt',
                'lt',
                'gte',
                'lte',
            ],
            'timestamp':[
                'exact',
                'gt',
                'lt',
                'gte',
                'lte',
                'year',
                'month',
            ],
        }

class RaspberryShakeQuakesFilter(django_filters.FilterSet):
    # online = django_filters.BooleanFilter(field_name="online")
    class Meta:
        model = RaspberryShakeQuakes
        fields = {
            'code': ['exact'],
            'depth':[
                'exact',
                'gt',
                'lt',
                'gte',
                'lte',
            ],
            'mag':[
                'exact',
                'gt',
                'lt',
                'gte',
                'lte',
            ],
            'timestamp':[
                'exact',
                'gt',
                'lt',
                'gte',
                'lte',
                'year',
                'month',
                'range',
            ],
        }