import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression

coffee_dataset=pd.read_csv('coffee_shop_sales.csv')

X=coffee_dataset.drop(columns='Daily Sales ($)', axis=1)
Y=coffee_dataset['Daily Sales ($)']

print(X)
print(Y)

scaler=StandardScaler()
standardized_data=scaler.fit_transform(X)

X=standardized_data
Y=coffee_dataset['Daily Sales ($)']

print(X)
print(Y)

X_train,X_test,Y_train,Y_test=train_test_split(X, Y, test_size=0.2)
#print(X.shape,X_train.shape,X_test.shape)

model=SVR(kernel='linear')
model.fit(X_train,Y_train)

lr_model=LinearRegression()
lr_model.fit(X_train,Y_train)

X_train_prediction=model.predict(X_train)
#print(X_train_prediction)
X_test_prediction=model.predict(X_test)
#print(X_test_prediction)

input_data=[200]     
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

std_data=scaler.transform(input_data_reshaped)
prediction=model.predict(std_data)

print("Predicted sales for given customers: $", prediction[0])

