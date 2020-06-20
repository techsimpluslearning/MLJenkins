from sklearn.datasets import load_iris
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


ts = open("TestSize.txt", "r")
ts =  float(ts.read()[:4])

iris = load_iris()
y_iris = iris.target
data = iris.data

trainX, testX, trainY, testY = train_test_split(data, y_iris, test_size = ts)
print("Training Your Machine...")
model = KNeighborsClassifier(n_neighbors=4)
model = model.fit(trainX, trainY)

print("Predict Your Data...")
pred = model.predict(testX)
accuracy = accuracy_score(pred, testY)
print(accuracy*100)
acc_file = open("accuracy.txt", "w")
acc_file.write(str(accuracy*100))
acc_file.close()


    

