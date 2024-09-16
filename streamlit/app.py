import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the model
modelPath = r'./model/output/modelLinearBrazil.pkl'
model = joblib.load(modelPath)

# Streamlit app
st.title('Model Cumulative Inflation Prediction')

# Input features
Year = st.number_input('Year', min_value=1980)
# feature2 = st.number_input('Feature 2', min_value=0)

# Convert input to DataFrame
input_data = pd.DataFrame([[Year]], columns=['Year'])

# Predict button
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write('Prediction:', prediction[0])
