#final result: dictionary w/ city names as keys, values: another dictionary containing: corresponding state, weather station, total precipitation per month (part 1), relative precipitation per month (part 2), total precipitation over the year (part 3), what proportion that is from all precipitation (part 3). 
#desired output after part 3: 
# {
#    "Cincinnati": {
#   "station": "GHCND:USW00093814",
#   "state": "OH",
#   "total_monthly_precipitation": [..],
#   "total_yearly_precipitation": ..,
#   "relative_monthly_precipitation": [..],
#   "relative_yearly_precipitation": ..
#   },
#   "Tucson": {..
#   },
#} 
#station code for Seattle: GHCND:US1WAKG0038
#dates: 2010-1 through 2010-12

import json 
import csv

with open('precipitation.json') as file: 
    precipitation = json.load(file)

from pandas import *
 
data = read_csv("stations.csv")
locations = data['Location'].tolist()
states = data['State'].tolist()
stations = data['Station'].tolist()

city_data = {}
index = 0 
for location in locations: 
    city_data[location] = {"station": stations[index], "state": states[index]}
    index = index + 1

precipitation_per_month = {}
total_monthly_precipitation = []

for measurement in precipitation: 
    if measurement["station"] == "GHCND:US1WAKG0038": 
        month = measurement["date"][:-3]
        if month in precipitation_per_month: 
            precipitation_per_month[month] = precipitation_per_month[month] + measurement["value"]
        else: 
            precipitation_per_month[month] = measurement["value"]

total_monthly_precipitation = list(precipitation_per_month.values())
city_data["Seattle"]["total_monthly_precipitation"] = total_monthly_precipitation
print(city_data)

with open('results.json', "w") as new_file:
    json.dump(city_data, new_file, indent = 4)