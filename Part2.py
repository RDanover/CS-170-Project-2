import pandas as pd
import sys 
import math

normalized_df = None

def train(training_data):
    print('Normalizing Data')
    global normalized_df
    columns_to_normalize = training_data.columns[1:]
    normalized_data = (training_data[columns_to_normalize] - training_data[columns_to_normalize].mean()) / training_data[columns_to_normalize].std()
    normalized_df = pd.concat([training_data.iloc[:, 0], normalized_data], axis=1)
    #normalized_df = training_data
    return

def test(test_index, test_data_set):
    test_vals = []
    i=0
    for value in test_index:
        if(i!=0):
            test_vals.append(value)
        else:
            i+=1
    distance_df=[]
    c=0
    for index, row in test_data_set.iterrows():
        i=-1
        euclidean_distance = 0
        for value in row:
            if(i!=-1):
                euclidean_distance+=(test_vals[i]-value)**2
            i+=1
        
        euclidean_distance = math.sqrt(euclidean_distance)
        if(index!=c):
            distance_df.append(10000000)
            c+=1
        distance_df.append(euclidean_distance)
        c+=1

    min=1000000
    i=0
    for distance in distance_df:
        if(distance<min):
            min = distance
            index_of_min = i
        i+=1
        
    return normalized_df.iloc[index_of_min, 0]

def evaluate(feature_set,full_data_set):
    feature_set = ['0'] + feature_set
    evaluation_df = full_data_set[feature_set]
    num_correct = 0
    num_total = 0
    train(evaluation_df)
    for index, row in normalized_df.iterrows():
        actual_class = normalized_df.iloc[index, 0]
        modified_df = evaluation_df.drop(index)
        predicted_class = test(row,modified_df)
        if(actual_class==predicted_class):
            num_correct+=1
        num_total+=1
    
    return num_correct/num_total



if len(sys.argv) < 4:
    print("Usage: python3 Part2.py <filepath> <number_of_features> <feature1> <feature2> . . . <featureN>")
    sys.exit(1)

filepath = sys.argv[1]
number_of_features = int(sys.argv[2])
set_of_features = []

for i in range(len(sys.argv)-3):
    set_of_features.append(str(sys.argv[i+3]))

column_names = [str(i) for i in range(0, number_of_features+1)]

df = pd.read_table(filepath, sep='\s+', names=column_names, header=None)

df = df.apply(pd.to_numeric, errors='coerce')

accuracy = evaluate(set_of_features, df)

print('Using Data Set:')
print(filepath)

print('And features:')
print(set_of_features)

print('We get an Accuracy of:')
print(accuracy)
