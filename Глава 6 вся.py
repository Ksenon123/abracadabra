import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn

df = pd.read_csv("heart.csv")
df

import seaborn as sns
sns.heatmap(df.corr())

from sklearn.model_selection import train_test_split

X = df.drop(["target"],axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 5)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
predictions

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(10,6))
ax1.set_title('Наши предсказания')
ax1.scatter(X_test['trestbps'], X_test['thalach'], c=predictions, cmap= 'tab10')
ax2.set_title('Реальные значения')
ax2.scatter(X_test['trestbps'], X_test['thalach'],c=y_test, cmap='tab10');

print("Accuracy:", model.score(X_test, y_test))

"""ДЕРЕВО РЕШЕНИЙ"""

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(max_depth=5)
clf = clf.fit(X_train,y_train)

prediction = clf.predict(X_test)

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(10,6))
ax1.set_title('Наши предсказания')
ax1.scatter(X_test['trestbps'], X_test['thalach'], c=predictions, cmap= 'tab10')
ax2.set_title('Реальные значения')
ax2.scatter(X_test['trestbps'], X_test['thalach'],c=y_test, cmap='tab10');

print("Accuracy:", clf.score(X_test, y_test))

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier()
mlp = mlp.fit(X_train, y_train)

prediction = mlp.predict(X_test)
print("Accuracy:", mlp.score(X_test, y_test))

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(10,6))
ax1.set_title('Наши предсказания')
ax1.scatter(X_test['trestbps'], X_test['thalach'], c=predictions, cmap= 'tab10')
ax2.set_title('Реальные значения')
ax2.scatter(X_test['trestbps'], X_test['thalach'],c=y_test, cmap='tab10');