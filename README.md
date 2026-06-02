# machine-learning-
machime learning mini projects
# TV Ad Budget vs Sales Prediction using Linear Regression

This project implements a simple **Linear Regression** model using **Scikit-Learn** to analyze and predict product sales based on the TV advertising budget. 

## Project Overview
The goal of this project is to understand the relationship between the money spent on TV commercials and the resulting product sales. It visualizes the data points, trains a linear model on 80% of the data, evaluates it on the remaining 20%, and makes predictions for new hypothetical budgets.

## Technologies Used
* **Python 3**
* **NumPy** & **Pandas** (Data manipulation and structuring)
* **Matplotlib** (Data visualization)
* **Scikit-Learn** (Model training, splitting, and evaluation)

## Dataset
The project reads data from a local file named `data.csv`. The dataset contains the following key columns:
* `TV Ad Budget ($)`: The independent variable ($X$) representing the marketing spend.
* `Sales ($)`: The dependent variable ($Y$) representing the revenue/sales generated.

## How It Works
1. **Data Visualization:** It plots a scatter plot using Matplotlib to see the distribution and trend of the data.
2. **Data Preprocessing:** Converts features into NumPy arrays and reshapes the feature $X$ to fit Scikit-Learn's requirements (`.reshape(-1, 1)`).
3. **Train-Test Split:** Splits the dataset into **80% Training data** and **20% Testing data**.
4. **Model Training:** Fits a `LinearRegression()` model on the training set.
5. **Evaluation:** Uses the `.score()` method to calculate the $R^2$ score (Accuracy) on the test set.
6. **Prediction:** Predicts the sales for new ad budgets: `$50`, `$100`, and `$200`.

## How to Run This Project

1. Clone the repository or download the files.
2. Make sure you have your `data.csv` in the same directory.
3. Install the required libraries if you haven't already:
   ```bash
   pip install numpy pandas matplotlib scikit-learn
