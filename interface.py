import streamlit as stl
import pickle as pk
import pandas as pd
import numpy as np


path ="model/diabetesV1.sav"
path_scale ="model/scale1.sav"
model = pk.load(open(path,'rb'))
scaling = pk.load(open(path_scale,'rb'))


def prediction(Preg,glu,bloodp,	SkinThick,Insulin,BMI,DiabetesPF,Age):
    dt_class=['Non diabétique', 'Diabétique']
    emoji = ['🤗😊','😔😓']
    input=scaling.transform([[Preg,glu,bloodp,	SkinThick,Insulin,BMI,DiabetesPF,Age]])
    input_shaped=np.reshape(input,(1,-1))
    value=model.predict(input_shaped)
    result=int(value[0])
    return result