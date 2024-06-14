from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from weatherapi.models import WeatherData
from weatherapi.serializers import WeatherDataSerializer, WeatherDataStatsSerializer
from rest_framework.response import Response

from django.db import transaction
from django.db.models import Sum, Avg
from django.db.models.functions import ExtractYear
from weatherapi.pagination import PageNumberPaginationn
from rest_framework import generics 


class WeatherDataView(generics.ListAPIView):
    
    pagination_class = PageNumberPaginationn
    serializer_class = WeatherDataSerializer
    queryset = WeatherData.objects.all()

class WeatherDataStatsView(generics.ListAPIView):
    
    pagination_class = PageNumberPaginationn
    serializer_class = WeatherDataStatsSerializer
    
    def get_queryset(self):
        weather_data_stats = WeatherData.objects.annotate(
            year=ExtractYear('date')
        ).values(
            'station_id', 'year'
        ).annotate(
            avg_max_temp=Avg('max_temperature'),
            avg_min_temp=Avg('min_temperature'),
            total_precipitation=Sum('precipitation')
        ).order_by('station_id', 'year')
        
        return weather_data_stats
    