def verif_new_data(t,h,p):
    n_clusters = centroids.shape[0]
    n_samples = data.shape[0];
    assign = {}
    clusters = {}
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
        
      
