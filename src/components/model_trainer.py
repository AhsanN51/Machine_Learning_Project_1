import os
import sys
from dataclasses import dataclass
from typing import Dict

from src.exception import CustomExceptionHandling
from src.logger import logging
from src.utils import save_object, evaluate_models

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)

from sklearn.metrics import r2_score


@dataclass
class ModelTrainerConfig:
    trained_model_filepath = os.path.join("model_data", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer = ModelTrainerConfig()

    def initiate_model_trainer(self, train_data_arr, test_data_arr):
        try:
            logging.info("Initiating model trainer.....")
            X_train, y_train, X_test, y_test = (
                train_data_arr[:, :-1],
                train_data_arr[:, -1],
                test_data_arr[:, :-1],
                test_data_arr[:, -1],
            )
            models = {
                "LinearRegression": LinearRegression(),
                "KNeighborsClassifier": KNeighborsClassifier(),
                "DecisionTreeClassifier": DecisionTreeClassifier(),
                # "XGBClassifier": XGBClassifier(),
                "CatBoostClassifier": CatBoostClassifier(verbose=False),
                "AdaBoostRegressor": AdaBoostRegressor(),
                "GradientBoostingRegressor": GradientBoostingRegressor(),
                "RandomForestRegressor": RandomForestRegressor(),
            }

            models_report: Dict[str, float] = evaluate_models(
                X_train, y_train, X_test, y_test, models=models
            )

            best_model_name, best_model_score = max(
                models_report.items(), key=lambda item: item[1]
            )

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomExceptionHandling("No best model found", sys)
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                path=self.model_trainer.trained_model_filepath,
                object=best_model,
            )

            predicted = best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)

            logging.info("Model training completed !!!")
            return r2_square

        except Exception as e:
            raise CustomExceptionHandling(e, sys)
