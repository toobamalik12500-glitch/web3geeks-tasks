# web3geeks-tasks
# Adult Income Prediction - Day 1

# Project Goal

The goal of this project is to predict if a person earns more than $50K per year.

* 0 = <=50K
* 1 = >50K

#Task 1: Problem Definition

We want to find people who are likely to earn more than $50K. We selected Precision as the main metric because we want to reduce wrong positive predictions.

#Task 2: Data Exploration

* Converted income into 0 and 1.
* Checked missing values and data types.
* Checked categorical columns and their values.
* Created histograms and bar plots.
* Created a simple summary table.

#Task 3: Train/Test Split

The data was divided into training data and test data in an 80/20 ratio. The test data will be used only for final evaluation.

## Task 4: Baselines

We created two simple baselines:

* **Majority baseline:** Always predicts <=50K.
* **Rule-based baseline:** Predicts >50K when education-num is 13 or more.

We checked their accuracy, precision, recall, F1, ROC AUC, PR AUC, and confusion matrices.

#Task 5: Error Analysis

We checked false positives and false negatives. We also found some data issues such as missing values, categorical data, skewed values, and extreme values.

#Results

* Majority baseline: **76.1% accuracy and 0% precision**
* Rule-based baseline: **75.3% accuracy and 48.4% precision**

#Main Metric

Precision will be our main metric because we want our >50K predictions to be more accurate.
