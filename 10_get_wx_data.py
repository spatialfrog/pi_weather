# TODO: create sqlite3 db
# TODO: write timestamp and humidity data
# TODO: connect with R to read using dplyr
# TODO: error handling i.e. missing values
# TODO: make script run at startup when pi rebooted etc


# create sqlite db to hold measurements
# http://www.blog.pythonlibrary.org/2012/07/18/python-a-simple-step-by-step-sqlite-tutorial/
# https://www.sqlite.org/datatype3.html
# http://pythoncentral.io/advanced-sqlite-usage-in-python/


import csv
import os
import sys
import time

from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()


# ### Write measurements to disk
# 
# * Write measurements to disk every `1 minute`.
# * Use CSV file format.
# * Timestamp with `ISO8601` format of `YYYY-hh-mmTHH:MM:SS`.
# 

def get_measurements():
    '''
    Return list of measurements
    
    Order of returned list is:
    * datetime, temp_humidity, temp_pressure, pressure and humidity
    
    Notes:
    * Numeric values rounded to 3 decimal places
    '''

    # clear previous data
    sense.clear()

    # generate iso8601 yyyy-mm-ddTHH:MM:SS timestamp string
    recorded_datetime = datetime.isoformat(datetime.now())

    # capture data from sensors
    temperature_from_humidity = round(sense.get_temperature_from_humidity(), 3)
    temperature_from_pressure = round(sense.get_temperature_from_pressure(), 3)
    pressure = round(sense.get_pressure(), 3)
    humidity = round(sense.get_humidity(), 3)
    
    return([recorded_datetime, temperature_from_humidity, temperature_from_pressure, pressure, humidity])


# ===== csv file

# output directory
output_directory = r'/home/pi/Projects/pi_weather/data/'

csv_file_name = 'raw.csv'

# full path to csv file
csv_path = os.path.join(output_directory, csv_file_name)

# csv column names
csv_headers = ['datetime', 'temperature_from_humidity', 'temperature_from_pressure', 'pressure', 'humidity']

# check if csv file exists
if os.path.exists(csv_path):
    pass
else:
    # create csv file on disk with headers
    with open(csv_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

# loop and read data every minute
while True:
    # get data
    data = get_measurements()
    
    # append data to csv
    #print(data)
    
    with open(csv_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    # wait 1 minute. function use seconds
    time.sleep(60)


