# -*- coding: utf-8 -*-
"""ASSIGNMENT: 202321

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aMvnLWDy-QyJv0At0Vs5CgYCfUXKPGXU

###**ASSIGNMENT: 202321**
Note: change the path of the csv file before running it.
The file is also uploaded in github as well.
"""

from google.colab import drive
drive.mount('/content/drive')

"""##**Ensemble Classifier**
#**1(a)**
"""

#self
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.utils import resample

class BaggingSoftmaxRegression:
    def __init__(self, n_models=10, sample_size=1.0):
        self.n_models = n_models
        self.sample_size = sample_size
        self.models = []
        for i in range(n_models):
            self.models.append(LogisticRegression(multi_class='multinomial', solver='lbfgs'))
            
    def fit(self, X, y):
        for model in self.models:
            X_sample, y_sample = resample(X, y, n_samples=int(self.sample_size*len(X)), replace=True)
            model.fit(X_sample, y_sample)
            
    def predict(self, X):
        predictions = np.zeros((X.shape[0], self.n_models))
        for i, model in enumerate(self.models):
            predictions[:,i] = model.predict_proba(X)[:,1]
        return np.argmax(predictions, axis=1)

"""**On given dataset impementation**"""

import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv("/content/drive/MyDrive/Sanskrit as NLP/program_data(unlabelled).csv")

X = df.drop("material", axis=1)  # Replace "target_variable_name" with the name of your target variable
y = df["material"] #if you change you will get different accuracy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

bagging = BaggingSoftmaxRegression(n_models=10, sample_size=0.8)
bagging.fit(X_train, y_train)
y_pred = bagging.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

"""#**1(b)**"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

# Load your dataset
df = pd.read_csv("/content/drive/MyDrive/Sanskrit as NLP/program_data(unlabelled).csv")

# Split the data into training and testing sets
X = df.drop("material", axis=1)  # Replace "target_variable_name" with the name of your target variable
y = df["material"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier
tree = DecisionTreeClassifier(max_depth=1)

# Fit the decision tree classifier on the training data
tree.fit(X_train, y_train)

# Create an AdaBoost classifier with 10, 25, and 50 iterations
boost_10 = AdaBoostClassifier(base_estimator=tree, n_estimators=10)
boost_25 = AdaBoostClassifier(base_estimator=tree, n_estimators=25)
boost_50 = AdaBoostClassifier(base_estimator=tree, n_estimators=50)

# Train the classifiers on the training data
boost_10.fit(X_train, y_train)
boost_25.fit(X_train, y_train)
boost_50.fit(X_train, y_train)

# Make predictions on the testing data
y_pred_single = tree.predict(X_test)
y_pred_boost_10 = boost_10.predict(X_test)
y_pred_boost_25 = boost_25.predict(X_test)
y_pred_boost_50 = boost_50.predict(X_test)

# Calculate the accuracy of each classifier
acc_single = accuracy_score(y_test, y_pred_single)
acc_boost_10 = accuracy_score(y_test, y_pred_boost_10)
acc_boost_25 = accuracy_score(y_test, y_pred_boost_25)
acc_boost_50 = accuracy_score(y_test, y_pred_boost_50)

# Print the results
print(f"Single decision tree accuracy: {acc_single}")
print(f"Boosting with 10 iterations accuracy: {acc_boost_10}")
print(f"Boosting with 25 iterations accuracy: {acc_boost_25}")
print(f"Boosting with 50 iterations accuracy: {acc_boost_50}")

"""#**2(a)**"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

# Load the data from a CSV file
df = pd.read_csv("/content/drive/MyDrive/Sanskrit as NLP/program_data(unlabelled).csv")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop("material", axis=1), df["material"], test_size=0.2, random_state=42)

# Create a logistic regression estimator
lr = LogisticRegression()

# Create an AdaBoost classifier with 50 estimators
ada = AdaBoostClassifier(base_estimator=lr, n_estimators=5)

# Fit the AdaBoost classifier to the training data
ada.fit(X_train, y_train)

# Make predictions on the testing data using the AdaBoost classifier
y_pred = ada.predict(X_test)

# Calculate the accuracy of the AdaBoost classifier
acc = accuracy_score(y_test, y_pred)

# Print the accuracy of the AdaBoost classifier
print("Accuracy for AdaBoost with 5 estimators:", acc)

"""#**2(b)**"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

# Load the data from a CSV file
df = pd.read_csv("/content/drive/MyDrive/Sanskrit as NLP/program_data(unlabelled).csv")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop("material", axis=1), df["material"], test_size=0.2, random_state=42)

# Create a logistic regression estimator
lr = LogisticRegression()

# Define the number of estimators to use
n_estimators = [10, 25, 50]

# Evaluate the AdaBoost classifier with different numbers of estimators
for n in n_estimators:
    # Create an AdaBoost classifier with n estimators
    ada = AdaBoostClassifier(base_estimator=lr, n_estimators=n)
    
    # Fit the AdaBoost classifier to the training data
    ada.fit(X_train, y_train)
    
    # Make predictions on the testing data using the AdaBoost classifier
    y_pred = ada.predict(X_test)
    
    # Calculate the accuracy of the AdaBoost classifier
    acc = accuracy_score(y_test, y_pred)
    
    # Print the accuracy of the AdaBoost classifier
    print("Accuracy for AdaBoost with", n, "estimators:", acc)

"""##**K Means Algorithm Problem**

#**1(a)**
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the text data
with open("/content/prgram_data.txt", "r") as f:
    text_data = f.readlines()

# Convert the text data to a numerical representation using the TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(text_data)

# Apply K-means clustering with K=3, 6, and 9
k_values = [3, 6, 9]
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
    labels = kmeans.labels_
    score = silhouette_score(X, labels)
    print(f"K={k}, Silhouette Score={score}")

"""#**1(B)**"""

import pandas as pd
from sklearn.cluster import KMeans

# Load the dataset from CSV file
df = pd.read_csv('/content/drive/MyDrive/Sanskrit as NLP/program_data(unlabelled).csv') #Remark: load your dataset here
df=df.drop("material",axis=1)

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

df = pd.read_csv('/content/drive/MyDrive/Sanskrit as NLP/program_data(unlabelled).csv')
# Extract the labels from the dataset
original_labels = df['material']

# Apply K-Means clustering for K=3, 6, and 9
for k in [3, 6, 9]:
    # Initialize the KMeans object
    kmeans = KMeans(n_clusters=k)
    
    # Fit the data to the KMeans object
    kmeans.fit(df.drop('material', axis=1)) # assuming 'label' is the name of the label column
    
    # Get the cluster labels
    cluster_labels = kmeans.labels_
    
    # Compute the accuracy for each cluster
    accuracies = []
    for i in range(k):
        indices = (cluster_labels == i)
        if indices.any():
            cluster_label_counts = original_labels[indices].value_counts()
            most_frequent_label = cluster_label_counts.index[0]
            predicted_labels = pd.Series([most_frequent_label] * indices.sum())
            accuracy = accuracy_score(original_labels[indices], predicted_labels)
            accuracies.append(accuracy)
        else:
            accuracies.append(0)
    
    # Compute the overall accuracy
    weights = [(cluster_labels == i).mean() for i in range(k)]
    overall_accuracy = sum([w * a for w, a in zip(weights, accuracies)])
    
    # Print the results
    print(f'K = {k}')
    print(f'Cluster accuracies: {accuracies}')
    print(f'Overall accuracy: {overall_accuracy}\n')