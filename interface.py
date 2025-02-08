import streamlit as stl
import pickle as pk


path ="model/diabetesV1.sav"
path_scale ="model/scale1.sav"
model = pk.load(open(path,'rb'))
scaler = pk.load(open(path_scale,'rb'))


def prediction()