import os
import sys

from sklearn.metrics import r2_score
import src.logger as logging
from src.exception import CustomException

import pandas as pd
import numpy as np
import dill

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        logging.error(f"Error occurred while saving object: {str(e)}")
        raise CustomException(e,sys)
    

def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report={}
        for i in range(len(models)):
            model=list(models.values())[i]
            model.fit(X_train,y_train)

            y_test_pred=model.predict(X_test)

            test_model_score=r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]]=test_model_score
        return report
    except Exception as e:
        logging.error(f"Error occurred while evaluating models: {str(e)}")
        raise CustomException(e,sys)