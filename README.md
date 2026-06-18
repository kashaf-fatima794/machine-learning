#  Machine Learning Mini Projects

Welcome to this collection of Machine Learning mini-projects! This repository showcases various implementations of **Regression** and **Classification** algorithms using Python and Scikit-Learn.

---

##  Projects Index
1. [ TV Ad Budget vs Sales Prediction (Linear Regression)](#1-tv-ad-budget-vs-sales-prediction)
2. [ Coffee Shop Sales Prediction (SVR & Linear Regression)](#2-coffee-shop-sales-prediction)
3. [ Customer Purchase Prediction (Gaussian Naive Bayes)](#3-customer-purchase-prediction)
4. [ Student Course Completion Prediction (Logistic Regression)](#4-student-course-completion-prediction)

---

## 1.  TV Ad Budget vs Sales Prediction

This project uses **Linear Regression** to analyze and predict product sales based on the TV advertising budget.

###  Key Features
* **Data Visualization**: Uses Matplotlib to plot trends and inspect data distribution.
* **Train-Test Split**: Dynamically splits data into **80% Training** and **20% Testing** sets.
* **Accuracy Evaluation**: Calculates the $R^2$ accuracy score to evaluate model performance.

###  Setup and Run
* **Dataset**: Requires a file named `data.csv`.
* **Execution**: Run the script to predict sales for budgets like `$50`, `$100`, and `$200`.

---

## 2.  Coffee Shop Sales Prediction

A project focusing on predicting a coffee shop's **Daily Sales ($)** based on operational features (like customer count) using multiple regression models.

###  Key Features
* **Feature Scaling**: Implements `StandardScaler` to normalize features for better optimization.
* **Multi-Model Training**: Fits and compares both **Support Vector Regressor (SVR)** and **Linear Regression**.
* **Live Prediction Pipeline**: Scales new user inputs on the fly for instant sales estimates.

###  Setup and Run
* **Dataset**: Requires `coffee_shop_sales.csv`.
* **Execution**: Pass an input (e.g., `[200]` customers) to get the predicted daily sales.

---

## 3.  Customer Purchase Prediction

A classification project using the **Gaussian Naive Bayes** algorithm to predict customer purchasing behavior based on demographics.

###  Key Features
* **Data Cleaning**: Automatically handles missing data points using `dropna()`.
* **Label Encoding**: Transforms categorical text (Gender, Income, etc.) into numeric values via `LabelEncoder`.
* **Probabilistic Modeling**: Uses `GaussianNB` to classify whether a customer will make a purchase.

###  Setup & Run
* **Dataset**: Requires `new_dataset_1000.csv`.
* **Execution**: Pass encoded customer profiles (e.g., `[[1, 0, 2, 1]]`) to get a `Yes/No` prediction.

---

## 4.  Student Course Completion Prediction

A classification project using **Logistic Regression** to predict whether a student will complete a course based on behavioral and performance metrics.

###  Key Features
* **Feature Separation**: Splits dataset dynamically into features (`X`) and the goal variable (`target` as `Y`).
* **Train-Test Evaluation**: Splits data into **80% Training** and **20% Testing**, then checks accuracy on both sets using `accuracy_score`.
* **Custom Prediction**: Includes an inference pipeline to test individual student profiles on the fly.

###  Setup & Run
* **Dataset**: Requires `student_course_data.csv`.
* **Execution**: Pass a 2D list of metrics (e.g., `[[study_hours, attendance, assignments, past_perf, motivation]]`) to predict course completion.

---
##  Common Technologies used
* **Python 3**
* **NumPy & Pandas** (Data manipulation)
* **Matplotlib** (Data visualization)
* **Scikit-Learn** (ML models, Preprocessing, and Evaluation)
* **NumPy & Pandas** (Data manipulation)
* **Matplotlib** (Data visualization)
* **Scikit-Learn** (ML models, Preprocessing, and Evaluation)
