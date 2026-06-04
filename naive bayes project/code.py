# Naive Bayes Project (Customer Purchase Prediction)

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("new_dataset_1000.csv")
print("Original Dataset (with missing values):")
print(df.head(10)) 
df = df.dropna()
print("\nDataset after dropping missing values:")
print(df.head(10)) 

gen_at = LabelEncoder()
age_at = LabelEncoder()
inc_at = LabelEncoder()
prev_at = LabelEncoder()

inputs = df.drop('Purchase', axis='columns')
target = df['Purchase']

inputs['Gender_n'] = gen_at.fit_transform(inputs['Gender'])
inputs['Age_n'] = age_at.fit_transform(inputs['AgeGroup'])
inputs['Inc_n'] = inc_at.fit_transform(inputs['Income'])
inputs['Prev_n'] = prev_at.fit_transform(inputs['PreviousPurchase'])

inputs_n = inputs.drop(['Gender', 'AgeGroup', 'Income', 'PreviousPurchase'], axis='columns')
print("\nEncoded Input Features:")
print(inputs_n.head(10)) 

classifier = GaussianNB()
classifier.fit(inputs_n, target)

accuracy = classifier.score(inputs_n, target)
print("\nModel Accuracy on full dataset:", accuracy)

# Predict for new customer
new_data = pd.DataFrame([[1, 0, 2, 1]], columns=['Gender_n', 'Age_n', 'Inc_n', 'Prev_n'])
prediction = classifier.predict(new_data)
print("\nPrediction (Will the customer purchase?):", prediction)
