"""Endpoint para cálculo de aderência."""
import pickle
import pandas as pd
import numpy as np
from fastapi import APIRouter
from scipy import stats
from pydantic import BaseModel


class Request(BaseModel):
    dataset_path: str

router = APIRouter(prefix="/aderencia")

def get_class1_scores(dataset_path, model):
    # Passa o dataset para um pandas dataframe para ser manipulado
    dataset_df = pd.read_csv(dataset_path, compression = 'gzip', dtype={"VAR45": 'str'})
    dataset_df.fillna(np.nan, inplace = True)
    
    if 'TARGET' in dataset_df:
        X = dataset_df.drop(columns='TARGET')
    else:
        X = dataset_df

    # Obtem uma lista da probabilidade de cada registro pertencer a classe 1
    predicted_y_class1 = model.predict_proba(X)[:, 1]
    return predicted_y_class1 

# Carregando préviamente os resultados das predições do dataset de teste
pickled_model = pickle.load(open('monitoring\model.pkl', 'rb'))
test_dataset_path = "datasets/credit_01/test.gz"
predicted_y_class1_test = get_class1_scores(test_dataset_path, pickled_model)

@router.post("/")
def calc_adherence(req: Request):
    # Obtendo as probabilidades referentes ao dataset da requisição 
    predicted_y_class1 = get_class1_scores(req.dataset_path, pickled_model)
    # Realizando o Kolmogorov-Smirnov test
    ks_res = stats.ks_2samp(predicted_y_class1_test, predicted_y_class1)
    return {"Adherence": ks_res}


