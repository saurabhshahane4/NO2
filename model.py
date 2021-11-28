import joblib
import xgboost
import os
import numpy as np


curr_path = os.path.dirname(os.path.realpath(__file__))
xgb = joblib.load('XGB')



def predict(attributes: np.array):
    
    pred = xgb.predict(attributes)

    print("Flux Value Predicted")

    return pred[0]
