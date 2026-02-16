import os
import sys
import dill

from src.exception import CustomExceptionHandling

import numpy as np
import pandas as pd

import pickle

from sklearn.metrics import r2_score

from src.logger import logging
from src.exception import CustomExceptionHandling


def save_object(path, object):
    try:

        dir_path = os.path.dirname(path)

        os.makedirs(dir_path, exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump(object, f)

    except Exception as e:
        raise CustomExceptionHandling(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models):

    try:
        logging.info("-> Evaluating models")
        report = {}
        for name, model in models.items():

            model.fit(X_train, y_train)
            logging.info(f"model {name} fitted.")
            y_test_pred = model.predict(X_test)

            report[name] = r2_score(y_test, y_test_pred)
            logging.info(f"model : {name} evaluated")

        logging.info("-> Evaluating models completed")
        return report
    except Exception as e:
        raise CustomExceptionHandling(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomExceptionHandling(e, sys)
