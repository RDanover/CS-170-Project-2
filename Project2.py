import pandas as pd
import numpy as np

print("Welcome to Rachel Danover's Feature Selection Algorithm.")
file_name = input("Type in the name of the file to test : ")
global df
df = pd.read_csv(file_name,sep=r'\s+',header=None)

def find_inverse_feature_set(feature_set):
    inverse_feature_set = []
    for i in range(feature_count):
        if(i+1 not in feature_set):
            inverse_feature_set.append(i+1)
    return inverse_feature_set

def train():
    global X_norm
    global y
    global feature_count
    X = df.iloc[:,1:]
    y = df.iloc[:,0]
    feature_count = len(X.axes[1])
    instance_count = len(X.axes[0])
    print("This dataset has ",feature_count," features (not including the class attribute), with ",instance_count ,"instances.")
    print("Please wait while I normalize the data...")
    means = X.mean()
    std = X.std()
    X_norm = (X - means)/std
    print("Done!")
    return 

def test():
    distances = np.sqrt(np.sum((train_x-test_X)**2,axis=1))     #Euclidean distance calculation axis needs to be 1 for correct element operations
    predicted_label_index = np.argmin(distances)                #Getting the index of the nearest neighbor for euclidean distance
    predicted_val = train_y.iloc[predicted_label_index]         #Getting Predicted value from the nn index
    return predicted_val

def evaluate(feature_set):
    inverse_feature_set = find_inverse_feature_set(feature_set)
    evaluate_df = X_norm.drop(inverse_feature_set,axis=1)
    global train_y
    global train_x
    global test_X
    global test_y
    total = 0
    correct = 0
    for index, row in evaluate_df.iterrows():
        train_x = evaluate_df.drop(index)  #Normalized dataset with the row at index 0 removed
        train_y = y.drop(index)       #y label at index droppped so predicted value from label is accurate
        test_X = evaluate_df.iloc[index].values.reshape(1,-1)   #Getting row value and reshaping it do for euclidean distance 
        test_y = y.iloc[index]                             # Getting the test value to compare with prediction
        predicted_class = test()
        if(predicted_class==test_y):
            correct+=1
        total+=1
    accuracy = correct/total
    return accuracy

train()
feature_set = [1,15,27]
accuracy = evaluate(feature_set)
print("Accuracy is: ",accuracy)






