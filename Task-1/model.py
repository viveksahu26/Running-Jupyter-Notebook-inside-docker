
import pandas as pd

#Reading from dataset

dataset = pd.read_csv("student_scores.csv")
print("DATASETS: ", dataset)
x, y = dataset["Hours"], dataset["Scores"]



#Providing algorithm" Linear Regression" to a machine, so that it become Intelligent

from sklearn.linear_model import LinearRegression
mind = LinearRegression()
x = x.values
x = x.reshape(25,1)
print("\nx.shape : " ,x.shape)
mind.fit(x,y)
print("Finally, cofficient/weight is : ",mind.coef_)
print("\nLet's check Intelligency of Machine..")
print("\nWhat will be the score if student studied for 5hrs: ", mind.predict([[5]]))


#Saving "trained-model" in a file, "experiencemodel.pk1"
import joblib
joblib.dump( mind, "experiencemodel.pk1")
