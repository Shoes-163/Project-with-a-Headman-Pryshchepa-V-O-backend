from django.db import models

class Devices(models.Model):
    name = models.CharField('Назва пристрою', max_length=70)
    is_working = models.BooleanField(default=True)

class Metrics(models.Model):
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    type_of_metrics = models.CharField('Тип метрики', max_length=50)
    value_of_metrics = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True
        )
    battery_level = models.PositiveSmallIntegerField()
