import numpy as np
import matplotlib.pyplot as plt
import math 

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

def kmeans(data, k):
    n_feats = data.shape[1]
    assign = {}
    
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
    return centroids, assignment
    
