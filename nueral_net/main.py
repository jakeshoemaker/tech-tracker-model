import pandas as pd
import numpy as np
import train
import preprocess
import model
import os
import argparse
from training import s3_helpers


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--data', type=str, required=True, help='provide the symbol of a publicly traded company. "Ex: GOOG"')
parser.add_argument('--ckpt', type=str, required=True, default="./checkpoints/generic.ckpt")


def predict(num_prediction, model, close_data, look_back):
    prediction_list = close_data[-look_back:]

    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        x = x.reshape((1, look_back, 1))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]

    return prediction_list


def predict_dates(num_prediction, dates):
    last_date = dates[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
    return prediction_dates


def main(data):
    train_generator, test_generator, close_train, close_test, date_train, date_test, close_data, dates = preprocess.preprocess(data)
    nn = model.get_model()
    trained_model = train.train(nn, train_generator)

    # serialize model 
    ckpt_path = './checkpoints/' + data + '.ckpt'
    weight = nn.save_weights(ckpt_path)
    # upload ckpt to s3 ---> can be loaded with model.load_weights() 
    s3_helpers.upload_file(ckpt_path, 'tt-model-weights')


    #look_back = 20
    #num_prediction = 30
    #forecast = predict(num_prediction, trained_model, close_data, look_back)
    #forecast_dates = predict_dates(num_prediction, dates)

    #for x in range(len(forecast)):
        #print('Date: ' + str(forecast_dates[x]) + ' Predicted Value: ' + str(forecast[x]))


if __name__=="__main__":
    args = parser.parse_args()
    main(args.data)