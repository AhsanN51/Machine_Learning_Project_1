import os
import sys
import dill

from src.exception import CustomExceptionHandling

import numpy as np
import pandas as pd

import pickle


def save_object(path, object):
    try:
        dir_path = os.path.dirname(path)

        os.makedirs(dir_path, exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump(object, f)

    except Exception as e:
        raise CustomExceptionHandling(e, sys)
