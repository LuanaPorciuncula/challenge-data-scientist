"""Endpoint para cálculo de Performance."""
import pandas as pd
import numpy as np
import pickle
from fastapi import APIRouter
from datetime import datetime
from sklearn.metrics import roc_auc_score
from typing import List
from registry import Registry

router = APIRouter(prefix="/performance")

@router.post("/")
def calc_performance(registries: List[Registry]):
    """Performance message."""
    pickled_model = pickle.load(open('monitoring\model.pkl', 'rb'))

    # Passa os registros para um pandas dataframe para ser manipulado
    batch_records = pd.DataFrame([registry.__dict__ for registry in registries])
    batch_records.fillna(np.nan, inplace = True)

    X = batch_records.drop(columns='TARGET')
    y = batch_records['TARGET']

    # Realiza o cálculo da performance
    predicted_y = pickled_model.predict_proba(X)
    performance = roc_auc_score(y, predicted_y[:, 1])

    # Realiza o cálculo da volumetria
    volumetry = {}
    
    for registry in registries:
        dt_obj = datetime.fromisoformat(registry.REF_DATE)
        month = str(dt_obj.month)+"-"+ str(dt_obj.year)
        if volumetry.get(month) is not None:
            volumetry[month] += 1
        else:
            volumetry[month] = 1

    return {"Volumetry": volumetry,
            "Performance": performance}