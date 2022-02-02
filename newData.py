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
        
      
