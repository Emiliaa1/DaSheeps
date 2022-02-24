from sense_hat import SenseHat
from logzero import logger, logfile
from time import sleep
import csv
from pathlib import Path
from datetime import datetime, timedelta
import numpy as np
from orbit import ISS
import math 
import sklearn.datasets as dataset


#Machine Learning clustering algorithm - Kmeans


#function that converts the data set csv to an array
def add_data():
    x = np.genfromtxt("Test.csv", delimiter = ",")
    return x

#bacteria_feats = generate_data(n_samples = 20, n_feats = 2)
bacteria_feats = add_data()


def verif_new_data(t,h,p):
    n_clusters = centroids.shape[0]
    #create our new data point
    new_data = [t,h,p]
    
    min_indx = -1
    min_val = 1000000
    #Search for the closest centroid
    for j in range(n_clusters):
        d = compute_distance(new_data,centroids[j])
        if d<min_val:
            min_val = d
            min_indx = j
            
    return min_indx

# function for the distance between 2 points
def compute_distance(x,y):
    dist = 0.0
    for(xx,yy) in zip(x,y):
        dist+=(xx-yy)**2
    return math.sqrt(dist)
    
#function for initialising the centroids
def random_init_clusters(data,n_clusters):
    #choose randomly n_clusters centroids from our data array
    indx = np.random.choice(range(data.shape[0]),n_clusters);
    #create an array for the centroids
    centroids = np.array([data[i] for i in indx])
    return centroids
    
def assign_clusters(data,centroids):
    #the sizes of the arrays
    n_clusters = centroids.shape[0]
    n_samples = data.shape[0];
    
    # array for keeping the index of the cluster assigned to each data point
    assign = {}
    #new array for keeping the data of each data point in the cluster
    clusters = {}
    
    for i in range(n_clusters):
        clusters[i] = []
    
    # iterating through the data array and searching the corresponding cluster for each data point
    for i in range(n_samples):
        min_indx = -1
        min_val = 1000000
        
        for j in range(n_clusters):
            d = compute_distance(data[i],centroids[j])
            if d<min_val:
                min_val = d
                min_indx = j
        assign[i] = min_indx
        clusters[min_indx].append(data[i])
    return assign, clusters

def update_centroids(clusters, n_clusters, n_feats):
    """ n_clusters = number of clusters
        n_feats = number of features
    """ 
    #create an array filled with zeros
    centroids = np.zeros((n_clusters,n_feats))
    #fill the centroids array with the average
    for i in range(n_clusters):
        centroids[i] = np.mean(clusters[i], axis=0)
    return centroids

#the kmeans function
def kmeans(data, k):
    n_feats = data.shape[1]
    assign = {}
    
    #calling the previous functions
    centroids = random_init_clusters(data, n_clusters = k)
    assign, clusters = assign_clusters(data, centroids)
    
    #the centroids update loop
    while(True):
        old_assign = assign
        centroids = update_centroids(clusters, k, n_feats)
        assign, clusters = assign_clusters(data, centroids)
        
        #the ending loop condition(if the centroids don't change anymore)
        if old_assign == assign:
            break
    return centroids, assign

#calling the function for the needed variables
np.random.seed(121)
#bacteria_feats is the csv
centroids, assignment = kmeans(bacteria_feats, k=5)




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
        header = ("Counter","Date/time","Latitude","Longitude","Temperature","Humidity","Barometic pressure","Cluster")
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
    #Reset the LED Matrix
    sense.clear()


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
        
        bacteria_found = verif_new_data(humidity,temperature,pressure)
        
        location = ISS.coordinates()
        data = (
            counter,
            datetime.now(),
            location.latitude.degrees,
            location.longitude.degrees,
            temperature,
            humidity,
            pressure,
            bacteria_found,
        )
        
        add_csv_data(data_file,data)
        #Display image on the matrix
        Sense_Hat_LEDMatrix(sense)
        
        #make a 15 seconds delay
        sleep(30)
        
        logger.info(f"iteration {counter}")
        counter += 1
        #Update time
        now_time = datetime.now()
        
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e}')
