from src.exception import CustomException
import pandas as pd
from src.logger import logging
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from src.utils import save_object
from sklearn.pipeline import Pipeline
import sys
from sklearn.compose import ColumnTransformer
import numpy as np
import os



            
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    def scalling_of_data(self):
        try:
            logging.info("Only scalling is required and encoding is not required as the data is already encoded")
            scaler=StandardScaler()
            numerical_cols=["age","cigsPerDay","totChol","sysBP","diaBP","BMI","heartRate","glucose"]
            categorical_columns=["BPMeds","education"] 
            num_pipeline=Pipeline(steps=[
                 ("filling missing values in muerical columns",SimpleImputer(strategy="median")),
                 ("Scalling of features",scaler)

            ])
            cat_pipeline=Pipeline(steps=[
                 ("filling missing values in categorical values",SimpleImputer(strategy="most_frequent"))
            ])
            preporcess=ColumnTransformer([
                 ("numerical_cloumns pe kaam hoga",num_pipeline,numerical_cols),
                 ("categorical-columns pe kaam hoga",cat_pipeline,categorical_columns)
            ])
            logging.info("we have done preprocessing")
            return preporcess
        except Exception as e:
             raise CustomException(e,sys)




    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            train_data=pd.read_csv(train_data_path)
            test_data=pd.read_csv(test_data_path)
            logging.info("we have obtained the dataset in data transformation class")
            logging.info("Now we are starting with scalling of data and filling of missing values")
            logging.info("dividing the data into dependent and independent features")
            input_train_features=train_data.drop("TenYearCHD",axis=1)
            input_test_features=test_data.drop("TenYearCHD",axis=1)
            output_train_features=train_data["TenYearCHD"]
            output_test_features=test_data["TenYearCHD"]
            logging.info("Scalling the data")
            preprocessor=self.scalling_of_data()
            logging.info("starting with preprocessor")
            input_scalled_train_features=preprocessor.fit_transform(input_train_features)
            logging.info("ended with fit_transformation")
            input_scalled_test_features=preprocessor.transform(input_test_features)
            logging.info("joing the dependent and independent features")
            final_train_data=np.c_[input_scalled_train_features,np.array(output_train_features)]
            final_test_data=np.c_[input_scalled_test_features,np.array(output_test_features)]
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor
            )
            return(final_test_data,final_train_data,self.data_transformation_config.preprocessor_obj_file_path)
        except Exception as e:
            raise CustomException(e,sys)
        



            




