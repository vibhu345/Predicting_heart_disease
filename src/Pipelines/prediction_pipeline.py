import os
import sys 
from src.exception import CustomException
from src.utils import load_object
import pandas as pd
import numpy as np

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self, male, age,education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes,
            totChol, sysBP, diaBP, BMI, heartRate,glucose):
        try:
            model_path=os.path.join("artifacts","trained_model.pkl")
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model=load_object(file_path=model_path)
            preprocessor=load_object(preprocessor_path)
            # Encode categorical variables
            male_encoded = 1 if male.lower() == "male" else 0
            currentSmoker_encoded = 1 if currentSmoker.lower() == "yes" else 0
            BPMeds_encoded = 1 if BPMeds.lower() == "yes" else 0
            prevalentStroke_encoded = 1 if prevalentStroke.lower() == "yes" else 0
            prevalentHyp_encoded = 1 if prevalentHyp.lower() == "yes" else 0
            diabetes_encoded = 1 if diabetes.lower() == "yes" else 0
            # Prepare features array
            custom_data_input_dict = {
            "male": [male_encoded],
            "age": [age],
            "currentSmoker": [currentSmoker_encoded],
            "cigsPerDay": [cigsPerDay],
            "BPMeds": [BPMeds_encoded],
            "prevalentStroke": [prevalentStroke_encoded],
            "prevalentHyp": [prevalentHyp_encoded],
            "diabetes": [diabetes_encoded],
            "education": [education],  # नया एट्रिब्यूट यहाँ जुड़ गया
            "totChol": [totChol],
            "sysBP": [sysBP],
            "diaBP": [diaBP],
            "BMI": [BMI],
            "heartRate": [heartRate],
            "glucose":[glucose]}
            df = pd.DataFrame(custom_data_input_dict)
            scaled_features = preprocessor.transform(df)
            result=model.predict(scaled_features)
            return result
        


            
        except Exception as e:
            raise CustomException(e,sys)
class CustomData:
    def __init__(self,gender:str,race_ethnicity:str,parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):
         self.gender = gender

         self.race_ethnicity = race_ethnicity

         self.parental_level_of_education = parental_level_of_education

         self.lunch = lunch

         self.test_preparation_course = test_preparation_course

         self.reading_score = reading_score

         self.writing_score = writing_score
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict={
                "gender":self.gender,
                 "race_ethnicity": self.race_ethnicity,
                "parental_level_of_education": self.parental_level_of_education,
                "lunch": self.lunch,
                "test_preparation_course": self.test_preparation_course,
                "reading_score": self.reading_score,
                "writing_score": self.writing_score

            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            return CustomException(e,sys)