from django.contrib.gis.db import models

# Create your models here.
class RaspberryShakeStations(models.Model):
    code = models.CharField(max_length = 10, null=False, primary_key=True)
    elev = models.DecimalField(max_digits=10, decimal_places=3)
    online = models.BooleanField(default=False)

    acc = models.DecimalField(max_digits=15, decimal_places=8, null=True)
    vel = models.DecimalField(max_digits=15, decimal_places=8, null=True)
    disp = models.DecimalField(max_digits=15, decimal_places=8, null=True)
    timestamp = models.DateTimeField()

    address = models.TextField(null=True)
    loc_pnt = models.PointField(null=True, blank=True)
    class Meta:
        db_table = 'rs_stations'

class RaspberryShakeQuakes(models.Model):
    code = models.CharField(max_length = 15, null=False, primary_key=True)
    depth = models.DecimalField(max_digits=15, decimal_places=6)
    mag = models.DecimalField(max_digits=8, decimal_places=6)

    timestamp = models.DateTimeField()
    agency = models.TextField(null=True)
    location = models.TextField(null=True)
    loc_pnt = models.PointField(null=True, blank=True)
    class Meta:
        db_table = 'rs_quakes'