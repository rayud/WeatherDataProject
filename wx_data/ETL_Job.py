import os 
import sys

sys.path.append(os.path.abspath('..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weatherproject.settings')

import django
import pandas as pd
import numpy as np
import json


django.setup()

from weatherapi.models import WeatherData



# def processing(weather_station) : 

#     file_path = weather_station

#     # Read the data into a Pandas dataframe
#     df = pd.read_csv(file_path,  sep=r'\s+', header=None, names=['date', 'max_temperature', 'min_temperature', 'precipitation'])

#     # Replace -9999 with NaN (null value)
#     df.replace(-9999, 0, inplace=True)

#     # Divide min_temperature, max_temperature, and precipitation by 10

#     df['min_temperature'] = df['min_temperature'] / 10.0
#     df['max_temperature'] = df['max_temperature'] / 10.0
#     df['precipitation'] = df['precipitation'] / 10.0
#     df['date'] = pd.to_datetime(df['date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
    
    


#     # Assign weather station ID
#     df['weather_station'] = file_path.split('.')[0]  # Replace 'Station A' with your actual weather station ID
#     # Display the transformed dataframe
#     print(f"{file_path}: {len(df)} records were ingested")
    
    
#     instances_to_create = [
#         WeatherData(
#             station_id=row['weather_station'],
#             date=row['date'],
#             max_temperature=row['max_temperature'],
#             min_temperature=row['min_temperature'],
#             precipitation=row['precipitation']
#         )
#         for row in df.to_dict('records')
#     ]   
    
     
#     try : 
#         with transaction.atomic():
#             WeatherData.objects.bulk_create(instances_to_create, ignore_conflicts=True)
#         print("Bulk create successfull")
#     except Exception as e :
#         print("Bulk create failed", e)



# current_dir = os.getcwd() 


# #Fetching all the files in wx_data folder
# files = os.listdir(current_dir)

# files.remove('test.py')

# for file in files : 
#     processing(file)


