from sense_hat import SenseHat
from logzero import logger, logfile
from time import sleep
import csv
from pathlib import Path
from datetime import datetime, timedelta
import numpy as np
#from orbit import ISS


#Set up a logfile

base_folder = Path(__file__).parent.resolve()

logfile(f"{base_folder}/events.log")

#initialise sense hat
sense = SenseHat()

#initialise csv file
data_file = base_folder/"data.csv"

def create_csv_file(data_file):
    #Create a new csv file and add the header row
    with open (data_file,'w') as f:
        writer = csv.writer(f)
        header = ("Counter","Date/time","Temperature","Humidity","Barometic pressure","Cluster")
        writer.writerow(header)

def add_csv_data(data_file, data):
    #Add a row of data to the data_file csv
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
"""
def Bacteria(sense):
    green = (43,107,76)
    sense.show_message("BACTERIA", text_colour = green)
"""

# function for displaying a drawing of a bacteria
def Sense_Hat_LEDMatrix(sense):
    #Define some colours
    e = [209,230,126]
    f = [104,222,124]
    g = [43,107,76]
    h = [0,0,0]
    
    #Create the image
    image = [
        h,h,h,h,h,h,h,h,
        h,h,h,f,f,h,h,h,
        h,h,f,g,g,f,h,h,
        h,h,f,e,g,f,h,h,
        h,h,f,g,g,f,h,h,
        h,h,f,g,e,f,h,h,
        h,h,h,f,f,h,h,h,
        h,h,h,h,h,h,h,h,
        ]
    #Display the image
    sense.set_pixels(image)
    sleep(3)
    #Reset the LED Matrix
    sense.clear()


#Bacteria(sense)
create_csv_file(data_file)
#Record the start and current time
start_time = datetime.now()
now_time = datetime.now()

counter = 1

#Run a loop for almost three hours
while(now_time < start_time + timedelta(minutes = 178)):
    try:
        #Get humidity, temperature and pressure
        humidity = round(sense.humidity,5)
        temperature = round(sense.temperature,5)
        pressure = round(sense.pressure, 5)
        
       # bacteria_found = verif_new_data(humidity,temperature,pressure)
        
       # location = ISS.coordinates()
        lat = 2
        long = 3
        data = (
            counter,
            datetime.now(),
            lat,
            long,
           # location.latitude.degrees,
            #location.longitude.degrees,
            temperature,
            humidity,
            pressure,
           # bacteria_found,
        )
        
        add_csv_data(data_file,data)
        #Display image on the matrix
        Sense_Hat_LEDMatrix(sense)
        
        #make a 5 minutes delay
        sleep(30)
        
        logger.info(f"iteration {counter}")
        counter += 1
        #Update time
        now_time = datetime.now()
        
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e}')
