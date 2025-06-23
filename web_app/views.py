from random import randrange, uniform
from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Devices, Metrics
from .serializers import DevicesSerializer, MetricsSerializer

class DevicesViewSet(viewsets.ModelViewSet):
    serializer_class = DevicesSerializer
    queryset = Devices.objects.all().order_by("id")

    def get_queryset(self):
        return Devices.objects

class MetricsViewSet(viewsets.ModelViewSet):
    serializer_class = MetricsSerializer
    queryset = Metrics.objects.all().order_by("id")

    def get_queryset(self):
        return Metrics.objects
    
    @action(detail=False, methods=['post'])
    def generate_metrics(self, request):
        with transaction.atomic():
            devices = Devices.objects.all()
            for i in devices:
                metrics = Metrics.objects.create(
                    device=i,
                    temperature=round(uniform(-20, 50), 1),
                    humidity=randrange(20, 90),
                    illumination=randrange(0, 1000),
                    pressure=randrange(950, 1050),
                    air_quality=randrange(0, 500),
                    carbon_dioxide_level=randrange(400, 2000),
                    wind_velocity=round(uniform(0, 20), 1),
                    noise=round(uniform(30, 120), 2),
                    battery_level=randrange(0, 100),
                )
                metrics.save
        return Response({'status': 'data generated'})