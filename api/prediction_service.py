from datetime import date, timedelta
from keras.models import Sequential
from keras.layers import LSTM, Dense
import math
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pandas_datareader as webreader
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow import keras


def get_prediction(market_id, prediction_id):
    """
    market_id : Specifies which trained model to load
    prediction_id : specify in (days) how many days to predict ahead
    """
    nasdaq_symbol = 'unknown rn'
    sp500_symbol = '^GSPC'
    today = date.today().strftime(r"%Y-%m-%d")
    start_date = "2020-06-01"
    scaler = MinMaxScaler(feature_range=(0, 1))

    if market_id == 'sp500':
        market_id = sp500_symbol
        model = tf.keras.models.load_model('sp500')
        print("model loaded")

        df = webreader.DataReader(market_id, data_source='yahoo', start=start_date, end=today)
        data = df.filter(['Close'])
        
        # get last 100 days & scale
        last_100 = data[-100:].values
        previous_close = last_100[-1]
        last_100_scaled = scaler.fit_transform(data[-100:].values)

        # creating the batch && reshaping
        X_test = []
        X_test.append(last_100_scaled)
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

        # get predicted scaled price and then inverse transform
        price = model.predict(X_test)
        price = scaler.inverse_transform(price)
        date_tomorrow = date.today() + timedelta(days=1)

        print(price)
        return price,previous_close
    else:
        print("unknown market_id")
        return ("error")
    




if __name__=="__main__":
    get_prediction('sp500', "1")
