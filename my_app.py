# Streamlit Documentation: https://docs.streamlit.io
import streamlit as st
import pandas as pd
import pickle

# Title/Text
st.title("Atoscout Project")
st.write("Welcome to Car Price Prediction Project.")

# Load the dataset
df = http://pd.read_csv("Ready_to_ML (1).csv")

# Display dataframe
st.header("Dataset Overview:")
st.dataframe(df.describe().T)

# Load machine learning model
filename = "my_model_Last"
model = pickle.load(open(filename, "rb"))

# User Inputs
st.sidebar.title("Feature Inputs:")
typee = st.sidebar.selectbox("Choose the type:", ["Used", "Pre-registered", "Demonstration", "Employee's car"])
make_model = st.sidebar.selectbox("Choose the make_model:", df["make_model"].unique())

power_kW = st.sidebar.number_input("Power (kW):")
engine_size = st.sidebar.number_input("Engine Size:")
mileage = st.sidebar.number_input("Mileage:")
age = st.sidebar.number_input("Age:")

# Create a dataframe using feature inputs
user_inputs = pd.DataFrame({
    "type": [typee],
    "make_model": [make_model],
    "power_kW": [power_kW],
    "engine_size": [engine_size],
    "mileage": [mileage],
    "age": [age],
})

# Display user inputs
st.header("User Inputs:")
st.table(user_inputs)

# Prediction with user inputs
predict = st.button("Predict")

if predict:
    prediction = model.predict(user_inputs)
    st.success(f"Predicted Price: {prediction[0]:,.2f} $")