import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import os

def load_model():
    df = pd.read_csv(os.path.join('data', 'data.csv'))
    X = df[['berat_buah', 'jarak', 'harga_bensin', 'cuaca', 'libur']]
    y = df[['persentase_cuaca', 'persentase_libur']]
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def predict_percentages(model, fruit_weights, distance, fuel_price, weather, holiday):
    features = np.array([[fruit_weights, distance, fuel_price, weather, holiday]])
    prediction = model.predict(features)[0]
    return prediction.tolist()
