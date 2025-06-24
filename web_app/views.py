from random import randrange, uniform
from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Devices, Metrics
from .serializers import DevicesSerializer, MetricsSerializer

class DevicesViewSet(viewsets.ModelViewSet):
    serializer_class = DevicesSerializer

    def get_queryset(self):
        return Devices.objects.all().order_by("id")

class MetricsViewSet(viewsets.ModelViewSet):
    serializer_class = MetricsSerializer

    def get_queryset(self):
        queryset = Metrics.objects.all().order_by('time')
        start_time = self.request.query_params.get('stime')
        end_time = self.request.query_params.get('etime')
        if start_time is not None:
            queryset = queryset.filter(time__gte=start_time)
        if end_time is not None:
            queryset = queryset.filter(time__lte=end_time)
        return queryset
    
    @action(detail=False, methods=['post'])
    def generate_metrics(self, request):
        with transaction.atomic():
            devices = Devices.objects.all()
            for i in devices:
                battery_level = randrange(0, 100)
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type_of_metrics='Температура, °C',
                    value_of_metrics=round(uniform(-20, 50), 1),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type_of_metrics='Вологість, %',
                    value_of_metrics=randrange(20, 90),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type_of_metrics='Рівень освітлення, lx',
                    value_of_metrics=randrange(0, 1000),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type_of_metrics='Тиск, гПа',
                    value_of_metrics=randrange(950, 1050),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type_of_metrics='Якість повітря (PM2.5), мкг/м³',
                    value_of_metrics=randrange(0, 500),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type_of_metrics='Рівень CO₂ в повітрі, ppm',
                    value_of_metrics=randrange(400, 2000),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type_of_metrics='Швидкість вітру, м/с',
                    value_of_metrics=round(uniform(0, 20), 1),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type_of_metrics='Рівень шуму, дБ',
                    value_of_metrics=round(uniform(30, 120), 2),
                )
                metrics.save
        return Response({'status': 'data generated'})
