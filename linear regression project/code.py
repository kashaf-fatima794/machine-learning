import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df=pd.read_csv("data.csv")

x=np.array(df['TV Ad Budget ($)']).reshape(-1, 1)
y=df['Sales ($)']

plt.scatter(x,y)
plt.xlabel("TV Ad Budget ($)")
plt.ylabel("Sales ($)")
plt.show()

x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2)

model=LinearRegression()
model.fit(x_train, y_train)

accuracy=model.score(x_test, y_test)
print(accuracy)

new_budgets=np.array([50, 100, 200]).reshape(-1, 1)
predicted_sales=model.predict(new_budgets)

print("TV Ad Budgets:",new_budgets.flatten())
print("Predicted Sales:",predicted_sales)
