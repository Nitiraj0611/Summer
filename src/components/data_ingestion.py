import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            cloud_config = {'secure_connect_bundle': 'C:\\Users\\Nitiraj\\Dropbox\\PC\\Desktop\\Summer\\Summer\\src\\resources\\secure-connect-nitiraj-singh-chouhan .zip'
}
            auth_provider = PlainTextAuthProvider('FBmZKgnOLNCKdZsxrupyDxvT', 'Qd2bed6nzj,_pCewHcD_WSQ7pfpx6x.RtboNBzgPmuoTh6BDZh5r9G9m2Qfrq-Pb+LaPMSB2uTMljEig7uabHqZ2XoeozE19uEMLmLkIN+dKJofroUPP7hcbPGMi+8Ln')

            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect('nitiraj')  # Replace 'your_keyspace' with your actual keyspace name

            query = "SELECT * FROM insurance"  # Replace 'your_table' with your actual table name
            rows = session.execute(query)

            df = pd.DataFrame(list(rows))
            logging.info('Fetched the data from Cassandra')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=4)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))







    