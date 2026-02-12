import os
import sys
from dataclasses import dataclass

from src.exception import CustomExceptionHandling
from src.logger import logging

from sklearn.model_selection import train_test_split
import pandas as pd

from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("model_data", "train.csv")
    test_data_path: str = os.path.join("model_data", "test.csv")
    raw_data_path: str = os.path.join("model_data", "raw.csv")


class DataIngestion:

    def __init__(self):
        self.ingestionConfig = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Initiating data ingestion...")
        try:
            data = pd.read_csv("notebook\data\preprocessed_data.csv")
            logging.info("Data successfully ingested!")

            os.makedirs(
                os.path.dirname(self.ingestionConfig.train_data_path), exist_ok=True
            )

            data.to_csv(self.ingestionConfig.raw_data_path, index=False, header=True)

            logging.info("Initiating train-test split...")
            train_data, test_data = train_test_split(
                data, test_size=0.2, random_state=42
            )
            train_data.to_csv(
                self.ingestionConfig.train_data_path, index=False, header=True
            )
            test_data.to_csv(
                self.ingestionConfig.test_data_path, index=False, header=True
            )
            logging.info("Train-Test split successfully completed!")

            logging.info("Data ingestion successfully completed!")

            return (
                self.ingestionConfig.train_data_path,
                self.ingestionConfig.test_data_path,
            )
        except Exception as e:
            raise CustomExceptionHandling(e, sys)


if __name__ == "__main__":
    data_ingest = DataIngestion()
    train_data, test_data = data_ingest.initiate_data_ingestion()

    data_transformer = DataTransformation()
    train_data_arr, test_data_arr, _ = data_transformer.initiate_data_transformation(
        train_data, test_data
    )
