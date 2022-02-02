bacteria_feats = []

#Open the machine learning training data    
def open_ml_data_csv(bacteria_feats):
    with open("Training_data.csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
        for row in reader: # each row is a list
            bacteria_feats.append(row)
