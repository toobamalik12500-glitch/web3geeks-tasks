# Adult Income Classification Project

 1 Project Objective

The objective of this project is to build a machine learning classification model that predicts whether a person's income is greater than $50K or not.

The project includes data preprocessing, feature engineering, model training, hyperparameter tuning, model evaluation, error analysis, feature interpretation, and production-ready inference.

 2 Dataset Description

The dataset contains information about people's demographic and employment characteristics.

Some important features include:

 Age
 Workclass
 Education
 Education Number
 Marital Status
 Occupation
 Relationship
 Race
 Sex
 Capital Gain
 Capital Loss
 Hours per Week
 Native Country

3 Target Variable

The target variable represents income.

 0 = Income less than or equal to $50K
1 = Income greater than $50K

 4 Feature Engineering

The following new features were created:

 age_group
 hours_group
 has_capital_gain
log_capital_gain
 higher_education
 education_hours_interaction

These features were created to provide additional information to the model.
5 Preprocessing

The following preprocessing steps were used:

Missing numerical values were filled using the median.
 Missing categorical values were filled using the most frequent value.
 Numerical features were standardized using `StandardScaler`.
 Categorical features were converted into numerical form using `OneHotEncoder`.
 Unknown categories were handled using `handle_unknown='ignore'`.

Feature engineering and preprocessing were included inside the machine learning pipeline.

6 Models Tested

The following classification models were tested:

1 Logistic Regression
2 Random Forest
3 Gradient Boosting

Gradient Boosting was selected as the final model after model comparison and tuning.

7 Hyperparameter Tuning

GridSearchCV was used for hyperparameter tuning of the Gradient Boosting model.

The parameters tested included:

Learning rate
Number of estimators
Maximum depth

Stratified 5-fold cross-validation was used during tuning.

8 Best Parameters

The best parameters found were:

* Learning rate: `0.1`
* Maximum depth: `5`
* Number of estimators: `200`

9 Selected Final Model

The selected final model is:

Gradient Boosting Classifier

The preprocessing and feature engineering steps are included in the same pipeline as the model.

10 Classification Threshold

The selected classification threshold is:

0.3

If the predicted probability is 0.3 or higher, the final prediction is `1`. Otherwise, the prediction is `0`.

11 Final Test Performance

The final model was evaluated on the unseen test data.

| Metric      |  Score |
| ----------- | -----: |
| Accuracy    | 0.8558 |
| Precision   | 0.6615 |
| Recall      | 0.8139 |
| F1 Score    | 0.7298 |
| ROC-AUC     | 0.9291 |
| PR-AUC      | 0.8329 |
| Brier Score | 0.0870 |

The model achieved an accuracy of approximately **85.6%** and a ROC-AUC of approximately **92.9%**.

12 Important Features

The most important features identified by the Gradient Boosting model were:

1. `marital-status_Married-civ-spouse`
2. `education-num`
3. `log_capital_gain`
4. `education_hours_interaction`
5. `capital-gain`
6. `capital-loss`
7. `age`
8. `fnlwgt`
9. `occupation_Exec-managerial`
10. `occupation_Other-service`

The most influential feature was `marital-status_Married-civ-spouse`.
13. Known Limitations

 The model can make incorrect predictions.
 False positives and false negatives are present.
 Some demographic features may introduce bias.
 Feature importance shows which features are useful for prediction but does not prove that they directly cause higher income.
The model performance may change on a different dataset or population.
14. How to Reproduce Training

To reproduce the project:

1 Load the dataset.
2 Separate the features and target variable.
3 Split the data into training and test sets.
4 Create the feature engineering steps.
5 Create the preprocessing pipeline.
 Train the classification models.
7 Tune the Gradient Boosting model using GridSearchCV.
Select the best model.
9 Evaluate the final model on the unseen test data.
10 Save the final pipeline as `final_model.pkl`.

 15 How to Run Inference

The saved model can be loaded using Joblib.

```python
import joblib

model = joblib.load("final_model.pkl")
```

New data can then be passed directly to the pipeline:

```python
probability = model.predict_proba(new_data)[:, 1]

prediction = (probability >= 0.3).astype(int)

print(probability)
print(prediction)
```

The pipeline automatically performs the required feature engineering and preprocessing. No manual preprocessing is required during inference.

16 Python and Library Versions

The project was developed using:

* Python: `3.12.10`
* Pandas: `3.0.5`
* NumPy: `2.5.2`
* Scikit-learn: `1.9.0`
* Joblib: `1.6.0`

17  Conclusion

The Gradient Boosting model performed well on the unseen test data. It achieved approximately 85.6% accuracy and 92.9% ROC-AUC.

The model was also tested using new unseen examples through the saved pipeline. The same preprocessing and feature engineering were automatically applied during inference.
