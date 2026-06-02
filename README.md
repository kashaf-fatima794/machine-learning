# 🤖 Machine Learning Mini Projects

Welcome to the Machine Learning Mini Projects repository! This repo contains simple, hands-on implementations of various Machine Learning models using Python and Scikit-Learn to solve real-world regression problems.

---

##  Projects Index
1. [Project 1: TV Ad Budget vs Sales Prediction](#1-tv-ad-budget-vs-sales-prediction-using-linear-regression)
2. [Project 2: Coffee Shop Sales Prediction](#2-coffee-shop-sales-prediction-using-svr--linear-regression)

---

## 1. TV Ad Budget vs Sales Prediction using Linear Regression

This project implements a simple **Linear Regression** model to analyze and predict product sales based on the TV advertising budget. 

###  Project Overview
The goal of this project is to understand the relationship between the money spent on TV commercials and the resulting product sales. It visualizes the data points, trains a linear model on 80% of the data, evaluates it on the remaining 20%, and makes predictions for new hypothetical budgets.

###  Dataset
The project reads data from a local file named `data.csv`. The dataset contains:
* `TV Ad Budget ($)`: The independent variable ($X$) representing the marketing spend.
* `Sales ($)`: The dependent variable ($Y$) representing the revenue/sales generated.

###  How It Works
1. **Data Visualization:** Plots a scatter plot using Matplotlib to see the distribution and trend of the data.
2. **Data Preprocessing:** Converts features into NumPy arrays and reshapes the feature $X$ to fit Scikit-Learn's requirements (`.reshape(-1, 1)`).
3. **Train-Test Split:** Splits the dataset into **80% Training data** and **20% Testing data**.
4. **Model Training:** Fits a `LinearRegression()` model on the training set.
5. **Evaluation:** Uses the `.score()` method to calculate the $R^2$ score (Accuracy) on the test set.
6. **Prediction:** Predicts the sales for new ad budgets: `$50`, `$100`, and `$200`.

---

## 2. Coffee Shop Sales Prediction using SVR & Linear Regression

This project focuses on predicting the **Daily Sales ($)** of a coffee shop based on operational features (like customer footfall) using multiple regression algorithms.

###  Project Overview
Unlike simple regression, this project applies **Feature Scaling** to normalize data and implements two different algorithms: **Support Vector Regressor (SVR)** with a linear kernel and **Linear Regression**, allowing for model comparison.

###  Dataset
The script expects a dataset named `coffee_shop_sales.csv` in the project directory. The dataset contains:
* **Target Variable:** `Daily Sales ($)` ($Y$)
* **Feature Variables:** Operational metrics like customer count ($X$)

###  How It Works
1. **Feature Scaling:** Uses `StandardScaler()` to normalize features to zero mean and unit variance, which is crucial for SVR performance.
2. **Train-Test Split:** Dynamically splits data into training (80%) and testing (20%) sets.
3. **Multi-Model Training:** Fits both `SVR(kernel='linear')` and `LinearRegression()` on the standardized training data.
4. **Single-Instance Prediction:** Takes a raw user input (e.g., `[200]` customers), transforms it using the pre-fitted scaler, and outputs the predicted sales.

---

##  Technologies & Libraries Used
All projects in this repository are built using Python and the following core data science libraries:
* **NumPy** & **Pandas** (Data manipulation, structuring, and array operations)
* **Matplotlib** (Data visualization and plotting)
* **Scikit-Learn** (Data preprocessing, train-test splitting, and ML modeling)

   ```bash
   git clone [https://github.com/your-username/machine-learning-.git](https://github.com/your-username/machine-learning-.git)
   cd machine-learning-
