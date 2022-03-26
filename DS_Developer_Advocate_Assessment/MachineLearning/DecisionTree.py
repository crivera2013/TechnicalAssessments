"""
Vanguard Technical Assessment (Data Scientist / Data Engineer)

Purpose: To have the candidate display a fundamental knowledge of
        machine learning algorithms and how to implement them
        with speed and efficiency.

Task: Code a Decision Tree algorithm without the aid of Machine
        Learning packages.
"""

import datetime as dt
from math import sqrt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


class DecisionTree:
    """
    Complete the following methods:
        - __init__ -> initialize the variables you think you will need
        - train_tree -> takes in two numpy arrays as inputs (inputs, outputs)
                        and creates a tree graph using an information gain formula of your choosing.
                        You should also be able to tune the leaf node size of the tree.
        - predict -> Takes in a numpy array and returns an array of predictions

    The speed of the decision tree and mean squared error score of the tree will be recorded.
    """

    def __init__(self):
        """ Create the object variables you believe you need"""

        pass


    def train_tree(self, inputs, outputs, min_leaf_size=10):
        """
        inputs - a numpy array
        outputs - a numpy array
        min_leaf_size - an integer determining the minimum number of records
                        a node needs in order to be further split.
        """

        pass


    def predict(self, inputs):
        """
        This function takes a numpy array, and given the decision tree structure
        created by the train_tree method, creates a new numpy array of predictions
        and returns those predictions
        inputs - a numpy array
        """

        pass

##############################################################################
##############################################################################
##### Test code below executed with python DecisionTree.py
##############################################################################
##############################################################################
def test_model(data, random_state, min_leaf_size):
    """
    Test the DecisionTree class on multiple parameters
    with multiple inputs.
    DO NOT MODIFY
    """
    # split the data into train and test subsets
    # with the random state set, the output will be the same every time
    x_train, x_test, y_train, y_test = train_test_split(data[:, :-1],
                                                        data[:, -1],
                                                        test_size=0.2,
                                                        random_state=random_state)
    # Start the timer
    start = dt.datetime.now()
    # Create the model
    tree_model = DecisionTree()
    # train the model
    tree_model.train_tree(x_train, y_train, min_leaf_size=min_leaf_size)
    # create predictions
    predictions = tree_model.predict(x_test)
    # record speed time
    speed = (dt.datetime.now() - start).total_seconds()

    #record root mean squared error
    rmse = round(sqrt(mean_squared_error(y_test, predictions)), 2)

    return [random_state, min_leaf_size, rmse, speed, predictions]


def main():
    """
    DO NOT MODIFY
    """
    wine_data = pd.read_csv("winequality-white.csv", sep=";").values

    tests = [[20, 10], [30, 10], [20, 20], [30, 20]]

    results = [test_model(wine_data, i[0], i[1]) for i in tests]

    for i in range(4):
        print("Test Model {0}:".format(i))
        print("RMSE: {0}".format(results[i][2]))
        print("Speed: {0} seconds".format(results[i][3]))
        print("*"*20)

if __name__ == "__main__":
    main()
