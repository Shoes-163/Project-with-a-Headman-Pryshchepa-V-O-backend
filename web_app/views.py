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
        device = self.request.query_params.get('device')
        queryset = Metrics.objects.all().order_by('time')
        queryset = queryset.filter(device=device)
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
            devices = Devices.objects.all().filter(is_working=True)
            for i in devices:
                battery_level = randrange(0, 100)
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type='temperature',
                    value=round(uniform(-20, 50), 1),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type='humidity',
                    value=randrange(20, 90),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type='illumination',
                    value=randrange(0, 1000),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type='pressure',
                    value=randrange(950, 1050),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type='air_quality',
                    value=randrange(0, 500),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type='carbon_dioxide_level',
                    value=randrange(400, 2000),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type='wind_velocity',
                    value=round(uniform(0, 20), 1),
                )
                metrics.save
                metrics = Metrics.objects.create(
                    device=i,
                    battery_level=battery_level,
                    type='noise_level',
                    value=round(uniform(30, 120), 2),
                )
                metrics.save
        return Response({'devicesNumber': len(devices),
                         'metricsNumber': len(devices)*8})
    
    @action(detail=False, methods=['get'])
    def types(self, request):
        queryset = Metrics.objects.all().order_by('time')
        type = request.GET.getlist('type')
        if len(type):
            queryset = queryset.filter(type__in=type)
        return Response(queryset.values())
