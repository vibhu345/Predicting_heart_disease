 # training the model
from sklearn.model_selection import train_test_split
import pandas as pd
# from Catboost import CatBoostClassifier
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from src.exception import CustomException
import sys
from src.utils import save_object
from src.logger import logging
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from src.utils import evaluate_models
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import os
class ModelTrainingConfig:
    trained_model_config=os.path.join("artifacts","trained_model.pkl")
class ModelTrainer:
    def __init__(self):
        self.model_train_config=ModelTrainingConfig()
    def initiate_model_training(self,test_array,train_array):
        try:
            logging.info("Started model training")
            x_train,y_train,x_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Decision Tree": DecisionTreeClassifier(),
                    "Random Forest": RandomForestClassifier(),
                    "Gradient Boosting": GradientBoostingClassifier(),
                    "Logistic Regression": LogisticRegression(),
                    "XGBClassifier": XGBClassifier(),
                    "AdaBoost Classisifer": AdaBoostClassifier(),
                }
            params={
                    "Decision Tree": {
                        'criterion':["ginni", "log","entropy"],
                        # 'splitter':['best','random'],
                        # 'max_features':['sqrt','log2'],
                    },
                    "Random Forest":{
                        # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    
                        # 'max_features':['sqrt','log2',None],
                        'n_estimators': [8,16,32,64,128,256]
                    },
                    "Gradient Boosting":{
                        # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                        'learning_rate':[.1,.01,.05,.001],
                        'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                        # 'criterion':['squared_error', 'friedman_mse'],
                        # 'max_features':['auto','sqrt','log2'],
                        'n_estimators': [8,16,32,64,128,256]
                    },
                    "Logistic Regression":{},
                    "XGBClassifier":{
                        'learning_rate':[.1,.01,.05,.001],
                        'n_estimators': [8,16,32,64,128,256]
                    },
                    
                    "AdaBoost Classisifer":{
                        'learning_rate':[.1,.01,0.5,.001],
                        # 'loss':['linear','square','exponential'],
                        'n_estimators': [8,16,32,64,128,256]
                    }
                    
                }
            report={}
            for i in range(len(list(models.values()))):
                model=list(models.values())[i]
                para=params[list(models.keys())[i]]
                gs=GridSearchCV(model,para,cv=5)
                gs.fit(x_train,y_train)
                model.set_params(**gs.best_params_)
                model.fit(x_train,y_train)
                y_train_pred=model.predict(x_train)
                y_test_pred=model.predict(x_test)
                train_model_score=accuracy_score(y_train,y_train_pred)
                test_model_score=accuracy_score(y_test,y_test_pred)
                report[list(models.keys())[i]]=test_model_score
            best_model_score=max(sorted(report.values()))
            best_model_name=list(report.keys())[list(report.values()).index(best_model_score)]
            best_model=models[best_model_name]
            logging.info("This is the best model till now",best_model)
            best_params=params[best_model_name]
            if best_model_score<=0.6:
                raise CustomException("NO BEST MODEL FOUND PLZ WORK HARD")
            logging.info("Best model verfied")
            save_object(file_path= self.model_train_config.trained_model_config,obj=best_model)
            logging.info("predicting using best model")
            predicted=best_model.predict(x_test)
            accuracy=accuracy_score(y_test,predicted)
            return accuracy
        except Exception as e:
            raise CustomException(e,sys)



# python -m src.components.data_ingestion