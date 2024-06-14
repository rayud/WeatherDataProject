from rest_framework import serializers
from weatherapi.models import WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta: 
        model = WeatherData
        # fields = "__all__"
        exclude = ['id']
        
class WeatherDataStatsSerializer(serializers.Serializer):
    station_id = serializers.CharField(max_length=100)
    year = serializers.IntegerField()
    avg_max_temp = serializers.DecimalField(max_digits=8, decimal_places=2)
    avg_min_temp = serializers.DecimalField(max_digits=8, decimal_places=2)
    total_precipitation = serializers.DecimalField(max_digits=8, decimal_places=2)