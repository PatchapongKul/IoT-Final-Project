#Importing relevant modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import joblib

# put data in dataframe
df = pd.read_csv('train_set.csv')
df.drop(columns=['Date','Time'],axis=1, inplace=True)

# split into features (X) and target (y)
X = df.drop(['Room_Occupancy_Count'], axis=1)
y = df[['Room_Occupancy_Count']]

# Scaling the dataset
# scaler = StandardScaler()
# scaler.fit(X)
# print("mean", scaler.mean_)
# print("std", scaler.scale_)
# X_scaled = scaler.fit_transform(X)

# After analysis, we will use ['S1_Temp', 'S1_Light', 'S3_Light', 'S1_Sound', 'S5_CO2_Slope'] as features
corr_features = ['S1_Temp', 'S1_Light', 'S3_Light', 'S1_Sound', 'S5_CO2_Slope']
X_final = X[corr_features]

X_train, X_test, y_train, y_test = train_test_split(X_final, y, test_size=0.25, random_state=42)

knn_model = KNeighborsClassifier(n_neighbors= 3, 
                                 p= 1, 
                                 weights="distance")
knn_model.fit(X_train, y_train)

print("Accuracy on test set: ", knn_model.score(X_test, y_test))
y_pred = knn_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize = (6,4))

sns.heatmap(cm, 
            annot=True, 
            cmap="Spectral",
            fmt='g'
           )
plt.xlabel('Predicted', fontsize=10)
plt.ylabel('Actual/Observed', fontsize=10)
plt.show()

print("================ Accuracy Report ================")
print(classification_report(y_test, y_pred))

knn_model_columns = list(X_train)
print(knn_model_columns)
joblib.dump(knn_model_columns, 'knn_model_columns.pkl')

joblib.dump(knn_model, 'knn_model.pkl')
print('Model dumped')