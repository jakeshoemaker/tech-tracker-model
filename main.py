from datetime import date, timedelta
from keras.models import Sequential
from keras.layers import LSTM, Dense
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as webreader
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# get today's date for data extraction
today = date.today().strftime(r"%Y-%m-%d")
start_date = "2010-01-01"

# getting s&p500 market data to train on
stockname = "S&P500"
symbol = '^GSPC'
df = webreader.DataReader(symbol, start=start_date, end=today, data_source="yahoo")

# getting the actual data we want to use
data = df.filter(['Close'])
np_data = data.values
# get num rows to split training data
training_data_length = math.ceil(len(np_data) * .80)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(np_data)

# data pre-processing --> need to split the data into mini batches
train_data = scaled_data[0:training_data_length, :]

# Split the data into x_train and y_train data sets
x_train = []
y_train = []
trainingdatasize = len(train_data) 
for i in range(100, trainingdatasize):
    x_train.append(train_data[i-100: i, 0]) #contains 100 values 0-100
    y_train.append(train_data[i, 0]) #contains all other values

# Convert the x_train and y_train to numpy arrays
x_train = np.array(x_train)
y_train = np.array(y_train)

# Reshape the data
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
#print(x_train.shape)
#print(y_train.shape)

### MODEL ARCHITECTURE ###
model = Sequential()

# Model with 100 nuerons - input shape = 100 timestamps
model.add(LSTM(100, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(100, return_sequences=False))
model.add(Dense(25, activation='relu'))
model.add(Dense(1))

# compile model
model.compile(optimizer='adam', loss='mean_squared_error')
print("model compiled")

# training the model
model.fit(x_train, y_train, batch_size=16, epochs=25)
