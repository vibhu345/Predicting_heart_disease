# The purpose of this file is to give us the path to test and train data file and we will give raw data to the file
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import sys
from src.exception import CustomException
from sklearn.utils import resample
from src.logger import logging
class DataIngestionConfig:
    # defining paths in this class
    train_data_path=os.path.join("artifacts","training_data_file.csv")
    test_data_path=os.path.join("artifacts","test_data_file.csv")
    raw_data_path=os.path.join("artifacts","raw_data_file.csv")
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("we have now entered into data ingestion wali class in dataingestion.py file")
        try:
            df=pd.read_csv("data\datasets_4123_6408_framingham.csv")
            logging.info("we have got the raw data")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("resampling of data")
            df_majority=df[df["TenYearCHD"]==0]
            df_minority=df[df["TenYearCHD"]==1]
            df_minority_upsampled=resample(df_minority,replace=True,n_samples=len(df_majority),random_state=1)
            df=pd.concat([df_majority,df_minority_upsampled])
            logging.info("we have done upsampling and starting with train test split")
            train_data,test_data=train_test_split(df,test_size=0.2,random_state=1)
            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("we have stored the train and test data path in the artifacts folder safely")
            return ( self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)
        except Exception as e:
            raise CustomException (e,sys)
        
if __name__=="__main__":
    obj1=DataIngestion()
    train_data_path,test_data_path=obj1.initiate_data_ingestion()


