from django.db import models

class Devices(models.Model):
    name = models.CharField('Назва пристрою', max_length=70)
    is_working = models.BooleanField(default=True)

class Metrics(models.Model):
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    type = models.CharField('Тип метрики', max_length=35)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    battery_level = models.PositiveSmallIntegerField()
