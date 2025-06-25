from rest_framework import serializers
from .models import Devices, Metrics

class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = '__all__'

class DevicesSerializer(serializers.ModelSerializer):
    metrics = MetricsSerializer(many=True, source="metrics_set")
    class Meta:
        model = Devices
        fields = ['id', 'name', 'is_working', 'metrics']
