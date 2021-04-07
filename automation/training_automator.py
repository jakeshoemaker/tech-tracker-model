import pandas as pd 
import numpy as np
import keras
import tensorflow as tf
import yfinance as yf
import argparse
import logging
import os
from nueral_net import main as m



""" The following program trains and stores trained models in a s3 bucket

:param model_list: a list of company tickers
:param bucket: the s3 bucket to upload to
:param object_name: the obejct name, if none then file name is used
:return: On success True, else False
"""

parser = argeparse.ArgumentParser("description tech tracker model trainer")
parser.add_argument('--models_path', type=str, default='../models.txt' ,required=False, help='The list of models you would like to train')

models = []

def get_list(model_path):
    with open(model_path) as f:
        for line in f:
            line = line.strip()
            models.append(line)
    return models

def main(models):
    for model in models:
        print("training {} and saving weights to s3" , model)
        m.main(model)

if __name__=="__main__":
    args = parser.parse_args()
    main(get_list(args.model_path))