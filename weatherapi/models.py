from django.db import models

class WeatherData(models.Model):
    station_id = models.CharField(max_length=50)
    date = models.DateField()
    max_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    min_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    precipitation = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta: 
        unique_together = ('station_id', 'date')

    def __str__(self):
        return f"Weather data for {self.date} at station {self.station_id}"
