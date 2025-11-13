import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import pickle

df = pd.read_csv('../dataset/advertising.csv')
df.head(5)

X = df[['TV','Radio','Newspaper']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

class MLR():
    def __init__(self):
        self.weights = None
    
    def fit(self,x_train,y_train):
        feature_matrix = np.c_[np.ones((1,x_train.shape[0])).T,x_train]

        # weights = (XᵀX)⁻¹ Xᵀy
        self.weights = np.linalg.inv(feature_matrix.T.dot(feature_matrix)).dot(feature_matrix.T).dot(y_train)

    def predict(self,x_test):
        feature_matrix = np.c_[np.ones((x_test.shape[0], 1)), x_test]

        return feature_matrix.dot(self.weights)
    

model = MLR()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

print("Weights (including bias):", model.weights)
print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

