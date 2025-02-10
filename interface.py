import streamlit as st
import pickle as pk
import pandas as pd
import numpy as np


path ="model/diabetesV1.sav"
path_scale ="model/scale1.sav"
model = pk.load(open(path,'rb'))
scaling = pk.load(open(path_scale,'rb'))


def prediction(Preg,glu,bloodp,	SkinThick,Insulin,BMI,DiabetesPF,Age):
    input=scaling.transform([[Preg,glu,bloodp,	SkinThick,Insulin,BMI,DiabetesPF,Age]])
    input_shaped=np.reshape(input,(1,-1))
    value=model.predict(input_shaped)
    result=int(value[0])
    return result

# Configuration de la page
st.set_page_config(page_title="Prédiction du Diabète", page_icon="🩺", layout="centered")

st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            color: white;
            background-color: #007BFF;
            padding: 10px;
            border-radius: 10px;
        }
        .info {
            text-align: center;
            font-size: 16px;
            color: white;
            background-color: #28a745;
            padding: 10px;
            border-radius: 10px;
        }
        body {
            background-image: url('output.jpg');
            background-size: cover;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.header("Explication des rubriques", divider='rainbow')
st.sidebar.markdown("""
    *Caractéristiques principales* :
    
    - **Grossesses**: Nombre de fois où l'on est enceinte.
    - **Glucose**: Concentration de glucose plasmatique sur 2 heures.
    - **Tension artérielle**: Pression artérielle diastolique (mm Hg).
    - **Épaisseur de la peau**: Épaisseur du pli cutané du triceps (mm).
    - **Insuline**: Insuline sérique de 2 heures (mu U/ml).
    - **IMC**: Indice de masse corporelle (poids en kg / taille en m²).
    - **DiabetesPedigreeFunction**: Score génétique du diabète.
    - **Âge**: Âge en années.
""")
 
# Interface principale
def main():
    st.markdown(
        """
        <h1 style="text-align:center; color: white; background-color:#87CEEB; padding: 15px; border-radius: 10px;">
            🩺 Système de Prédiction du Diabète chez Les femmes
        </h1>
        """, unsafe_allow_html=True
    )

    st.markdown(
        "<h4 style='text-align:center; color:gray;'>Analyse des facteurs de risque du diabète</h4>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.subheader("Entrez les valeurs suivantes :")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        grossesses = st.number_input("Grossesses", 0, 20, 1)
        glucose = st.slider("Glucose", 0, 300, 100)
        tension = st.slider("Tension artérielle", 0, 150, 70)
    
    with col2:
        peau = st.slider("Épaisseur de la peau", 0, 150, 20)
        insuline = st.slider("Insuline", 0, 900, 79)
        imc = st.slider("IMC", 0.0, 70.0, 25.0)
        
    with col3:
        pedigree = st.slider("DiabetesPedigreeFunction", 0.0, 2.5, 0.5)
        age = st.slider("Âge", 1, 120, 30)

    if st.button("Prédire le diabète", key='predict'):
        input_data = pd.DataFrame([[grossesses, glucose, tension, peau, insuline, imc, pedigree, age]],
                                  columns=["Grossesses", "Glucose", "Tension artérielle", "Épaisseur de la peau", 
                                           "Insuline", "IMC", "DiabetesPedigreeFunction", "Âge"])
        st.text("Tableau récapitilatif sur les différentes entrées")
        input_data
        result= prediction(grossesses, glucose, tension, peau, insuline, imc, pedigree, age)
        st.markdown(
            f"""
            <div class='main-container' style='background-color: {"#ff4d4d" if result == 1 else "#4CAF50"}; color: white;'>
                <h3>Résultat, C'est une : {'Diabétique' if result == 1 else 'Non diabétique'}</h3>
            </div>
            """, unsafe_allow_html=True
        )
if __name__ == "__main__":
    main()
