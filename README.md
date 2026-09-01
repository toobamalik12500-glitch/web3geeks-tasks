# web3geeks-tasks
# Adult Income Prediction - Day 2
Day 2 – Supervised Learning Models
Overview

In Day 2, I worked with the Adult Census Income dataset and built two supervised machine learning models. The main focus was on preprocessing mixed data, using pipelines, training models, and evaluating their performance on a hold-out test set.

Task 1: Preprocessing

The dataset contains both numeric and categorical features. For numeric features, I used median imputation followed by StandardScaler. For categorical features, I used most-frequent imputation followed by OneHotEncoder with handle_unknown='ignore'.

I used a ColumnTransformer and pipelines so that the same preprocessing steps were applied correctly and data leakage was avoided.

Task 2: Supervised Models

Two models were trained:

Logistic Regression
Decision Tree Classifier

Both models were trained only on the training data. The hold-out test data was kept separate for evaluation.

Task 3: Model Evaluation

Both models were evaluated using accuracy, precision, recall, F1 score, ROC AUC, PR AUC, ROC curves, Precision-Recall curves, and confusion matrices.

Results
Metric	Logistic Regression	Decision Tree
Accuracy	0.8524	0.8141
Precision	0.7414	0.6098
Recall	0.5885	0.6198
F1 Score	0.6562	0.6148
ROC AUC	0.9042	0.7475
PR AUC	0.7632	0.4690

Logistic Regression performed better on most metrics, while Decision Tree had slightly higher recall.

Task 4: Interpretability

For Logistic Regression, I examined the coefficients to identify the top positive and negative features.

For the Decision Tree, I checked its depth, training score, test score, and important features. The training score was 0.9999 and the test score was 0.8141, which suggests possible overfitting.

The three most important features found were:

marital-status_Married-civ-spouse
fnlwgt
education-num
Task 5: Model Selection

Based on the results, Logistic Regression was selected for further development. It achieved better overall performance and also provides easier interpretation through its coefficients.

For Day 3, I plan to test different preprocessing choices, especially different methods for handling missing categorical values. The preprocessing pipeline will also be reused for future models.

Conclusion

Day 2 helped me understand how preprocessing pipelines can be combined with supervised machine learning models. Logistic Regression was the stronger overall model based on the evaluation results, so it will be the main candidate for further improvement on Day 3.
