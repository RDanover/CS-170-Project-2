import pandas as pd
import numpy as np
import random

def find_most_common_class():
    count_A = 0
    count_B = 0
    for c in y:
        if(c==2.0):
            count_B+=1
        elif(c==1.0):
            count_A+=1
    if(count_A>count_B):
        return 1.0
    elif(count_B>count_A):
        return 2.0
    return -1

def find_inverse_feature_set(feature_set):
    inverse_feature_set = []
    for i in range(feature_count):
        if(i+1 not in feature_set):
            inverse_feature_set.append(i+1)
    return inverse_feature_set

def find_full_feature_set():
    full_feature_set = []
    for i in range(feature_count):
        full_feature_set.append(i+1)
    return full_feature_set

def train():
    global X_norm
    global y
    global feature_count
    X = df.iloc[:,1:]
    y = df.iloc[:,0]
    feature_count = len(X.axes[1])
    instance_count = len(X.axes[0])
    print("This dataset has",feature_count,"features (not including the class attribute), with",instance_count ,"instances.")
    print("\n")
    print("Please wait while I normalize the data...", end =" ")
    means = X.mean()
    std = X.std()
    X_norm = (X - means)/std
    print("Done!")
    print("\n")
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

def evaluate_empty(): #evaluates accuracy using predicted class always set to the most common class in the dataset
    global train_y
    global train_x
    global test_X
    global test_y
    total = 0
    correct = 0
    most_common_class = find_most_common_class()
    for c in y:
        test_y = c
        predicted_class = most_common_class
        if(predicted_class==test_y):
            correct+=1
        total+=1
    accuracy = correct/total
    return accuracy


def greedy_forwards(full_feature_set):
    current_accuracy = 0
    temp_accuracy = 0
    initial_state = []
    options = full_feature_set.copy()  # Use copy to avoid modifying the original list
    temp = []
    queue = []
    max_accuracy = evaluate_empty() * 100
    best_feature_subset = []
    
    print("Running nearest neighbor with no features (default rate), using “leaving-one-out” evaluation, I get an accuracy of {:.1f}%".format(max_accuracy))
    print("\n")

    for feature in full_feature_set:
        temp.append(feature)
        queue.append(temp.copy())
        temp = []

    max_number_of_features = len(full_feature_set)
    print("Beginning search.")
    print("\n")
    for k in range(max_number_of_features):
        if k > 0:
            queue = []
            for feature in options:
                temp = initial_state.copy()  # Use copy to avoid modifying the original list
                temp.append(feature)
                queue.append(temp.copy())

        for feature_sub_set in queue:
            temp_accuracy = evaluate(feature_sub_set) * 100
            print("\tUsing feature(s) {", end="")
            print(*feature_sub_set, sep=",", end="")
            print("}",end="")
            print(" accuracy is {:.1f}%".format(temp_accuracy))

            if temp_accuracy >= current_accuracy:
                temp_best_feature_subset = feature_sub_set.copy()
                current_accuracy = temp_accuracy
        
        print("\n")
        if current_accuracy < max_accuracy:
            print("(Warning, Accuracy has decreased! Continuing search in case of local maxima)")
        else:
            best_feature_subset = temp_best_feature_subset.copy()
            max_accuracy = current_accuracy

        initial_state = temp_best_feature_subset.copy()
        options = [f for f in options if f not in temp_best_feature_subset]  # Remove selected features from options
        
        print("Feature set {", end="")
        print(*initial_state, sep=",", end="")
        print("}",end="")
        print(" was best, accuracy is {:.1f}%".format(current_accuracy))
        print("\n")
        current_accuracy = 0

    print("Finished search!! The best feature subset is {", end="")
    print(*best_feature_subset, sep=",", end="")
    print("}",end="")
    print(", which has an accuracy of {:.1f}%".format(max_accuracy))

    return


def greedy_backwards(full_feature_set):
    current_accuracy = 0
    max_accuracy = 0
    temp_accuracy = 0
    initial_state = full_feature_set.copy()
    temp=initial_state.copy()
    queue = []
    queue.append(temp.copy())
    best_feature_subset = []

    max_number_of_features = len(full_feature_set)
    print("Beginning search.")
    print("\n")
    for k in range(max_number_of_features):
        if k > 0:
            queue = []
            for i in range(len(initial_state)):
                temp = initial_state.copy()
                temp.pop(i)
                queue.append(temp.copy())

        for feature_sub_set in queue:
            temp_accuracy = evaluate(feature_sub_set) * 100
            print("\tUsing feature(s) {", end="")
            print(*feature_sub_set, sep=",", end="")
            print("}",end="")
            print(" accuracy is {:.1f}%".format(temp_accuracy))

            if temp_accuracy >= current_accuracy:
                temp_best_feature_subset = feature_sub_set.copy()
                current_accuracy = temp_accuracy
        
        print("\n")
        if current_accuracy < max_accuracy:
            print("(Warning, Accuracy has decreased! Continuing search in case of local maxima)")
        else:
            best_feature_subset = temp_best_feature_subset.copy()
            max_accuracy = current_accuracy

        initial_state = temp_best_feature_subset.copy()
        
        print("Feature set {", end="")
        print(*initial_state, sep=",", end="")
        print("}",end="")
        print(" was best, accuracy is {:.1f}%".format(current_accuracy))
        print("\n")
        current_accuracy = 0

    temp_accuracy = evaluate_empty() * 100
    
    print("Running nearest neighbor with no features (default rate), using “leaving-one-out” evaluation, I get an accuracy of {:.1f}%".format(temp_accuracy))
    if temp_accuracy < max_accuracy:
        print("(Warning, Accuracy has decreased! Continuing search in case of local maxima)")
        print("\n")

    print("Finished search!! The best feature subset is {", end="")
    print(*best_feature_subset, sep=",", end="")
    print("}",end="")
    print(", which has an accuracy of {:.1f}%".format(max_accuracy))

    return

def randomChoice(full_feature_set,n,k):
    best_feature_subset = []
    feature_sub_set = []
    max_accuracy = 0
    for i in range (int(n)):
        feature_sub_set = random.sample(full_feature_set, int(k))
        temp_accuracy = evaluate(feature_sub_set) * 100
        print("Itteration:",i+1,"/",n)
        print("\n")
        print("\tUsing feature(s) {", end="")
        print(*feature_sub_set, sep=",", end="")
        print("}",end="")
        print(" accuracy is {:.1f}%".format(temp_accuracy))
        print("\n")
        if(temp_accuracy>=max_accuracy):
            max_accuracy=temp_accuracy
            best_feature_subset = feature_sub_set
        else:
            print("(Warning, Accuracy has decreased! Continuing search in case of local maxima)")
            print("\n")
    
    print("Finished search!! The best feature subset is {", end="")
    print(*best_feature_subset, sep=",", end="")
    print("}",end="")
    print(", which has an accuracy of {:.1f}%".format(max_accuracy))
    return


print("Welcome to Rachel Danover's Feature Selection Algorithm.")
file_name = input("Type in the name of the file to test : ")
global df
df = pd.read_csv(file_name,sep=r'\s+',header=None)
print("\n")
print("Type the number of the algorithm you want to run.")
print("\n")
print("\tForward Selection")
print("\tBackward Elimination")
print("\tRachel's Special Algorithm")
print("\n")
print("\t \t \t \t",end="")
algorithm_choice = input()
print("\n")


if(algorithm_choice=='1'):
    train()
    full_feature_set = find_full_feature_set()
    greedy_forwards(full_feature_set)
elif(algorithm_choice=='2'):
    train()
    full_feature_set = find_full_feature_set()
    greedy_backwards(full_feature_set)
elif(algorithm_choice=='3'):
    
    print("Please enter the number of restarts you would like to use:\n")
    n_choice = input()
    print("\n")
    print("Please enter the size of the feature subset you would like to use:\n")
    k_choice = input()
    print("\n")
    train()
    full_feature_set = find_full_feature_set()
    randomChoice(full_feature_set,n_choice,k_choice)





