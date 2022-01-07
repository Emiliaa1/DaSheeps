from sense_hat import SenseHat
from time import sleep
import csv
from pathlib import Path

sense = SenseHat()
data_file = base_folder/"data.csv"

def create_csv_file(data_file):
    #Create a new csv file and add the header row
    with open (data_file,'w') as f:
        writer = csv.writer(f)
        header = ("Counter","Date/time","Temperature","Humidity","Barometic pressure")
        writer.writerow(header)

def add_csv_data(data_file, data):
    #Add a row of data to the data_file csv
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        

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
    sense.clear()

Sense_Hat_LEDMatrix(sense)



