import pandas as pd
import numpy as np
import keras
from keras.preprocessing.sequence import TimeseriesGenerator
import yfinance as yf
from pandas_datareader import data as pdr

# steps:
# 1. get data
# 2. preprocess data using generators
# 3. train model
# 4. predict

# this process doesnt take a long time therefore it might be beneficial to just feed the model data and train it then get predicitions
# it makes sense right now at least haha!
# 
#
# python code: 
    # preprocess.py
    # model.py
    # train.py
    # predict.py

def preprocess(company_code):
    df = pdr.get_data_yahoo(company_code)

    # dropping the columns we dont need
    df.drop(columns=['Open', 'High', 'Low', 'Volume'], inplace=True)

    # we will be training the model on 80% and testing on 20%
    close_data = df['Close'].values
    close_data = close_data.reshape((-1,1))

    split_percent = 0.80
    split = int(split_percent*len(close_data))

    close_train = close_data[:split]
    close_test = close_data[split:]

    date_train = df.index[:split]
    date_test = df.index[split:]

    look_back = 20

    train_generator = TimeseriesGenerator(close_train, close_train, length=look_back, batch_size=20) 
    test_generator = TimeseriesGenerator(close_test, close_test, length=look_back, batch_size=1)

    return train_generator, test_generator, close_train, close_test, date_train, date_test, close_data, df.index
