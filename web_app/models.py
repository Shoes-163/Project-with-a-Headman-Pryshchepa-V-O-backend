from django.db import models

class Devices(models.Model):
    name = models.CharField('Назва пристрою', max_length=50)

class Metrics(models.Model):
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    temperature = models.DecimalField(
        max_digits=3, decimal_places=1, blank=True
        )
    humidity = models.PositiveSmallIntegerField(blank=True)
    illumination = models.PositiveSmallIntegerField(blank=True)
    pressure = models.PositiveSmallIntegerField(blank=True)
    air_quality = models.PositiveSmallIntegerField(blank=True)
    carbon_dioxide_level = models.PositiveSmallIntegerField(blank=True)
    wind_velocity = models.DecimalField(
        max_digits=3, decimal_places=1, blank=True
        )
    noise = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True
        )
    battery_level = models.PositiveSmallIntegerField()
