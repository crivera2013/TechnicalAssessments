# DS Developer Advocate Technical Assessment Questions
![alt text](https://cdn-images-1.medium.com/max/1200/1*Qi2ta02wgA4-otNFDaFrRw.png)

For this assessment, there are four questions below that cover the following topics:
1. Data Structures
2. Machine Learning
3. SQL
4. Data Visualization


Please answer the questions and return your results within 1 week as a zip file, **"candidate_name_DS_Developer_Advocate_Assessment"** (ex:  *donald_duck_DS_Developer_Advocate_Assessment.zip*).'


Candidates who pass the technical assignment, will also need to explain their submissions during the in-person interviews.

Any questions regarding the assessment can be sent to Christian Rivera, christian_rivera@merqube.com

## Data Structures Question
### Part A:
Write a function that takes as input a list of up to 1 million random integers and returns the number of unique integers in that list.
We are most interested in hearing your thoughts and ideas, more so than a perfect response of code.  As such, please show us your own implementation rather than something already existing and please avoid built-in evaluation expressions (No `len(set(inputs))` ).

Sample input : Sample output:

        [1, 2, 0] : 3

        [4, 1, 3, 4, 2, 3, 4] : 4


### Part B:
Can part A be done with `O(1)` auxiliary space (i.e. using only a constant amount of additional
memory)? If so, write a function that does it. If not, why not?

Write all of your code in the language of your choice in a file called `DataStructures.py` (or other file extension).


## Machine Learning Question
Without the aid of any ML packages, please code a Decision Tree algorithm.  You may use packages lke **NumPy** or other vectorization packages but you cannot use packages like **SciKit-Learn**.  Attached is starter code, `decisionTree.py` where you are expected to complete the `DecisionTree` class by completing the functions:
- `DecisionTree.train( train_x, train_y, min_leaf_size=10)`
- `DecisionTree.predict(test_x)`

Your decision tree will have only one hyperparameter, `min_leaf_size`, that determines the minimum number of records in a given leaf node necessary for it to branch off into child leaf nodes.  The logic for how your tree determines what variable and value a given node splits is up to you as well as what value an end leaf node should return (average output of the records? median? or another metric of your choosing).
Your code is expected to run without error when `decisionTree.py` and will be assessed on two metrics for each of the 4 test cases:
1. The root mean squared error of the model outputs
2. Training speed of the models


## SQL question
- Go to https://modeanalytics.com  and create a free account
- Open a SQL editor, and on the right search for a database called **tutorial.dc bikeshare q1 2012**
- Using that SQL table, determine what was the longest amount of time a single bike has gone without being ridden between rides
- Provide the bike ID and the amount of time in the file `SQLanswers.txt`
- Copy the SQL query used to procure that answer into the file `bikeQuery.sql`


## Data Visualization Question
Given the datasets found in the github project below on the 2019 Womens World Cup, create **2-3 visualizations (charts and/or tables)** that you believe display an interesting story (or stories) from the tournament dataset.  Provide the code for cleaning and creating the visualizations into a file called `visualizationGenerator.py` (or in another language if you wish).  The visualizations can be individual image files or embedded in a jupyter notebook or similar tools.

- [2019 Womens World Cup found here](https://github.com/rfordatascience/tidytuesday/tree/master/data/2019/2019-07-09)

Your visualizations will be assessed on 3 metrics:
1. Ease of Understanding
2. Degree of Difficulty
3. Aesthetic Appeal

## Data Processing Question
On your own machine, install Spark and create a jupyter notebook environment.  In either Scala or PySpark, load in the attached csv file and complete the following data cleaning task.  You will analyze `bitcoinotc.csv`.  This graph is a who-trusts-whom network of people who trade using Bitcoin on a platform called Bitcoin OTC. The dataset has three columns in the following format:
1. Source Node
2. Target Node
3. Edge Weight

The weighted-in-degree of a node is the sum of weights of all the incoming edges to a node. The weighted-out-degree is the sum of weights of all the outgoing edges from a node. Lastly, the weighted-total-degree of a node is the sum of its weighted-in-degree and its weighted-out-degree.

You will need to:
1. Eliminate duplicate edges
2. Filter the graph edges to remove any edge whose edge weight is less than 5
3. Find the node with highest weighted-in-degree, highest weighted-out-degree, and highest weighted-total-degree
4. Download your results into a csv file called "`graphResults.csv`" in the following format:

| Vertex ID | Weighted Degree Sum | Type                |
|-----------|---------------------|---------------------|
| 4         | 50                  | Weighted In-Degree  |
| 7         | 45                  | Weighted Out-Degree |
| 2         | 75                  | Total               |

5. Export your Jupyter notebook into a `.py` or `.scala` file called `graphProcessing.py` or `graphProcessing.scala`


# Submission
For submission, the file directory should look like this:

```
<_candidate_name>_<_position>_assessment
│   AL-ML Technical Assessment.html
│
└───DataStructures
│   │   DataStructures.py
│
└───MachineLearning
│   │   decisionTree.py
│   │   winequality-white.csv
│
└───SQL
│   │   SQLanswers.txt
│   │   bikeQuery.sql
│
└───DataVisualization
│   │   visualizationGenerator.py
│   │   image1.png, image2.png, image3.png (or notebook)

```
