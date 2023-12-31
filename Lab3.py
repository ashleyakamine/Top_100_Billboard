"""
 Name: Ashley & Heven 
 Assignment: Lab 3 - Process dataset
 Course: CS 330
 Semester: 2023
 Instructor: Dr. Cao
 Date: 10/10/2023
 Sources consulted: any books, individuals, etc consulted

 Known Bugs: description of known bugs and other program imperfections

 Creativity: anything extra that you added to the lab

 Instructions: instructions to user on how to execute your program
"""
import random
import sys
import argparse
import math
import csv

import pandas as pd  

def splitData(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store the first 7000 of them in trainData, and the rest 3000 in testData
    Instruction:
            There is no grading script for this function, because different group may select different dataset depending on their course project, but generally you should make sure that you code can divide the dataset correctly, since you may use it for the course project
    """
    # Handle error
    if ratio < 0 or ratio > 1:
        raise ValueError("Ratio should be between 0 and 1.")

    # Calculate the number of samples to use for training
    num_samples = len(data)
    num_train_samples = int(num_samples * ratio)

    # Split the data into training and test sets
    trainData.extend(data[:num_train_samples])
    testData.extend(data[num_train_samples:])


def splitDataRandom(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store 7000 of them in trainData, and 3000 in testData.
    Instruction:
            Almost same as splitData, the only difference is this function will randomly shuffle the input data, so you will randomly select data and store it in the trainData
    """
    if ratio < 0 or ratio > 1:
        raise ValueError("Ratio should be between 0 and 1.")
    
    random.shuffle(data)

    num_samples = len(data)
    num_train_samples = int(num_samples * ratio)

    trainData.extend(data[:num_train_samples])
    testData.extend(data[num_train_samples:])

def most_listened_performer(billboard_data):
    # Create a dictionary to store performer counts
    performer_counts = {}

     # Open and read the CSV file
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            performer = row['performer']
            if performer in performer_counts:
                performer_counts[performer] += 1
            else:
                performer_counts[performer] = 1

    # Find the performer with the highest count
    most_listened_performer = max(performer_counts, key=lambda x: performer_counts[x])

    return most_listened_performer

def calculate_correlations(data, column_pairs, method='pearson'):
    """
    Calculate correlations for specified column pairs in a DataFrame.
    Input:
        data (pd.DataFrame): The DataFrame containing the data.
        column_pairs (list of tuples): List of column pairs for which you want to calculate correlations.
    Output:
        dict: A dictionary where keys are the column pairs, and values are the corresponding correlation coefficients.
    Example: 
        calculate_correlations(file_path, [('weeks_on_chart', 'week_position')], method='pearson') would calculate the correlation 
        coeffiecient between 'weeks_on_chart' and 'week_position'
    """
    df = pd.read_csv(file_path)
    
    correlations = {}
    
    for pair in column_pairs:
        col1, col2 = pair
        correlation = df[col1].corr(df[col2], method='pearson')
        correlations[f"{col1} vs {col2}"] = correlation

    return correlations


file_path = r'.\data\billboard.csv'
most_listened = most_listened_performer(file_path)
print("The most-listened performer is:", most_listened)

correlations = calculate_correlations(file_path, [('week_position', 'previous_week_position'),])

for column_pair, correlation in correlations.items():
    print(f"Correlation for {column_pair}: {correlation}")

def main():
    options = parser.parse_args()
    mode = options.mode       # first get the mode
    print("mode is " + mode)
    """
    similar to Lab 2, please add your testing code here
    """
    if mode == "T":
        inputFile = options.input
        outModel = options.output
        if inputFile == '' or outModel == '':
            showHelper()
        # Train your model here

    elif mode == "P":
        inputFile = options.input
        modelPath = options.modelPath
        outPrediction = options.output
        if inputFile == '' or modelPath == '' or outPrediction == '':
            showHelper()
        # Make predictions using your model

    elif mode == "E":
        predictionLabel = options.input
        trueLabel = options.trueLabel
        outPerf = options.output
        if predictionLabel == '' or trueLabel == '' or outPerf == '':
            showHelper()

def showHelper():
    """
    Similar to Lab 2, please update the showHelper function to show users how to use your code
    """
    parser.print_help(sys.stderr)
    # your code here

    sys.exit(0)

if __name__ == "__main__":
    #------------------------arguments------------------------------#
    #Shows help to the users                                        #
    #---------------------------------------------------------------#
    parser = argparse.ArgumentParser()
    parser._optionals.title = "Arguments"
    parser.add_argument('--mode', dest='mode',
    default = '',    # default empty!
    help = 'Mode: R for random splitting, and N for the normal splitting')

    """
    Similar to Lab 2, please update the argument, and add as you need
    """
    # your code here
    if len(sys.argv)<3:
        showHelper()
    main()