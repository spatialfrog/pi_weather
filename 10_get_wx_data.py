import datetime as datetime
import sqlite3
from sense_hat import SenseHat

# TODO: create sqlite3 db
# TODO: write timestamp and humidity data
# TODO: connect with R to read using dplyr
# TODO: error handling i.e. missing values
# TODO: make script run at startup when pi rebooted etc


# create sqlite db to hold measurements
# http://www.blog.pythonlibrary.org/2012/07/18/python-a-simple-step-by-step-sqlite-tutorial/
# https://www.sqlite.org/datatype3.html
# http://pythoncentral.io/advanced-sqlite-usage-in-python/


sense = SenseHat()
sense.clear()

# get time stamp of measurement
measurement_stamp = datetime.datetime.isoformat(datetime.datetime.now())

# get pressure in mb
pressure = sense.get_pressure()

# round to 3 decimal places
round_pressure = round(pressure, 3)

# print time of measurement and humidity
print(measurement_stamp, round_pressure)
