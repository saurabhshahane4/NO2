# pip install streamlit
import streamlit as st
from model import predict
import numpy as np

st.set_page_config(page_title="Agricultural N2O Flux Prediction App",
                   page_icon="🔫", layout="wide")

feats = ['Year', 'DataUse', 'Month', 'Vegetation', 'N_rate', 'PP2', 'PP7',
       'AirT', 'DAF_TD', 'DAF_SD', 'WFPS25cm', 'NH4', 'NO3', 'Clay', 'SOM']

with st.form("prediction_form"):

    st.header("Enter the Deciding Factors:")

    year = st.slider("Year: ", 2002, 2017, value=2002, format="%d")
    datause = st.number_input("Datause: (0 or 1)")
    month = st.slider("Month: ", 1, 12, value=0, format="%d")
    veg = st.multiselect("Vegetation: ",  ["Corn", "GLYMX", "TRIAE"])
    nrate = st.number_input("N_rate: ")
    pp2 = st.number_input("PP2: ")
    pp7 = st.number_input("PP7: ")
    airt = st.number_input("AirT: ")
    daft = st.number_input("DAF_TD: ")
    dafs = st.number_input("DAF_SD: ")
    wfps = st.number_input("WFPS25cm: ")
    nh4 = st.number_input("NH4: ")
    no3 = st.number_input("NO3: ")
    clay = st.number_input("Clay: ")
    som = st.number_input("Soil Organic Matter: ")

    submit_val = st.form_submit_button("Predict Flux")

if submit_val:
    # If submit is pressed == True
    print(veg)
    crop = {"Corn": 1, "GLYMX": 2, "TRIAE": 3}
    veg =  crop[veg[0]]
    attribute = np.array([year, datause, month,
                        veg, nrate, pp2, pp7, airt,
                        daft, dafs, wfps, nh4, no3, clay, som]).reshape(1,-1)


    
    print("attrubutes valid")
    

    value = predict(attributes= attribute)


    st.header("Here are the results:")
    st.success(f"The Flux predicted is {value}")