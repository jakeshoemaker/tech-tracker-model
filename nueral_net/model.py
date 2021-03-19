from keras.models import Sequential
from keras.layers import LSTM, Dense

def get_model():
    look_back = 20

    model = Sequential()
    model.add(
        LSTM(10,
            activation='relu',
            input_shape=(look_back, 1))
    )
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')

    return model