from rest_framework import serializers
from .models import Devices, Metrics

class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = '__all__'
        extra_kwargs = {
            'time': {'required': False},
            'temperature': {'required': False},
            'humidity': {'required': False},
            'illumination': {'required': False},
            'pressure': {'required': False},
            'air_quality': {'required': False},
            'carbon_dioxide_level': {'required': False},
            'wind_velocity': {'required': False},
            'noise': {'required': False},
        }
    
    def create(self, validated_data):
        return super().create(validated_data)

class DevicesSerializer(serializers.ModelSerializer):
    metrics = MetricsSerializer(many=True, source="metrics_set")
    class Meta:
        model = Devices
        fields = ['id', 'name', 'metrics']
    
    def create(self, validated_data):
        return super().create(validated_data)
    