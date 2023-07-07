from bottle import Bottle, run, request
import json
import numpy as np
import joblib
import time
import csv
import pandas as pd
from sklearn.preprocessing import RobustScaler

app = Bottle()
acertosT = 0
total = 0
TotReq = 0

scaler = joblib.load('/root/classificador/scaler.pkl')  # Carregar o scaler a partir do arquivo joblib
classificador = joblib.load('/root/classificador/svm.joblib')  # Carregar o modelo de classificação a partir do arquivo joblib

@app.route('/clasificar', method='POST')
def alarma():
    global classificador
    global scaler
    global acertosT
    global total
    global TotReq

    data = json.load(request.body)
    df = np.asarray(data, dtype=np.float64)  # Converter em array numpy

    z = df.shape
    features = df[0:z[0]-1, 0:z[1]-1]
    features_reordered = features.copy()
    features_reordered[:, [0, 2]] = features_reordered[:, [2, 0]]
    df_features = np.asarray(features_reordered, dtype=np.float64)

    tags = np.array(df[0:z[0]-1, z[1]-1].T, dtype=int)

    features_N = scaler.transform(df_features)
    y = classificador.predict(features_N)

    trues = np.sum(y == tags)

    acertosT += trues
    total += len(y)

    print("Classificação:", y)
    print("Real: ", tags)
    print("acertos: ", acertosT, "errados: ", total - acertosT, "acuracia: ", acertosT/total)
    print("--------------------------------------------------")

    TotReq += 1


def run_server():
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print("An exception occurred:", str(e))


if __name__ == "__main__":
    run_server()
