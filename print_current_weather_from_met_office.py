"""
This is a simple example which will print out the current weather and
temperature for our location.

Requirements: pip install datapoint

records:
    date
    time
    location
    description
    temperature (degrees C)
    feels-like temperature (degrees C)
    humidity
    precipitation
    wind speed (mph)
    wind gust (mph)
    wind direction

"""


import csv
import datapoint
from time import gmtime, strftime
from time import sleep

def get_current_weather(time_now, loc, conn):
    # Print date and time
    print(time_now, end=',')

    # Get nearest site and print out its name
    
    no_data_retrieved = True
    
    # Sometimes Datapoint fails to return data. 
    # Keep in loop until data returned
    
    attempts = 0
    while no_data_retrieved:
        try:           
            site = conn.get_nearest_forecast_site(loc[1],loc[2])
            
            # Get a forecast for the nearest site
            forecast = conn.get_forecast_for_site(site.id, "3hourly")
            now = forecast.now()
    
            print(loc[0], end=',')
            print(now.weather.text, end=',')
            print(now.temperature.value, end=',')
            print(now.feels_like_temperature.value, end=',')
            print(now.humidity.value, end=',')
            print(now.precipitation.value, end=',')
            print(now.wind_speed.value, end=',')
            print(now.wind_gust.value, end=',')
            print(now.wind_direction.value)
            no_data_retrieved = False
            
            # Give up after 100 attempts (just print location)
            attempts += 1
            if attempts == 100:
                    print(loc[0], end=',')
                    no_data_retrieved = False
        
        except:
            # Re-establish connection
            conn = datapoint.Manager(
                    api_key="fa81416c-a56a-4360-b9cf-ff11fe68113f")
            pass

    return

def main():
    time_now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    
    # Read in API key
    with open('api_key.txt', 'r') as f:
        key = f.readline()
    
    # Establish connection
    conn = datapoint.Manager(api_key = key)
      
    # Get weather for each city
    with open('./data/city_list.csv') as cities_csv:
        reader= csv.reader(cities_csv)
        # Skip the header
        next(reader, None)
        for row in reader:
            city = row[0]
            lat = float(row[1])
            long = float (row[2])
            location = (city, long, lat)
            get_current_weather(time_now, location, conn)
            
if __name__ == '__main__':
    main()
