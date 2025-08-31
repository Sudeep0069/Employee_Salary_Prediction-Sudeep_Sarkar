import joblib
import pandas as pd
import streamlit as st

# Load trained model and mappings
model = joblib.load("best_model.pkl")
mappings = joblib.load("mappings.pkl")

st.set_page_config(page_title="Employee Salary Prediction", page_icon="🪙", layout="centered")
st.title("🪙 Employee Salary Prediction App")
st.markdown("Predict if you earn >50k or <=50k:")

# Sidebar inputs
st.sidebar.header("Input Employee Details")

age = st.sidebar.slider("Age", 18, 65, 25)
workclass = st.sidebar.selectbox("Workclass", list(mappings["workclass"].keys()))
fnlwgt = st.sidebar.selectbox("fnlwgt", list(mappings["fnlwgt"].keys()))
education = st.sidebar.selectbox("Education Level", list(mappings["educational-num"].keys()))
marital = st.sidebar.selectbox("Marital Status", list(mappings["marital-status"].keys()))
occupation = st.sidebar.selectbox("Occupation", list(mappings["occupation"].keys()))
gender = st.sidebar.selectbox("Gender", list(mappings["gender"].keys()))
relationship = st.sidebar.selectbox("Relationship", list(mappings["relationship"].keys()))
race = st.sidebar.selectbox("Race", list(mappings["race"].keys()))
country = st.sidebar.selectbox("Country", list(mappings["native-country"].keys()))
hours_per_week = st.sidebar.slider("Hours per week", 1, 80, 40)
capt_gain = st.sidebar.slider("Capital Gain", 0, 100000, 0)
capt_loss = st.sidebar.slider("Capital Loss", 0, 5000, 0)

# Build input dataframe using mappings
input_df = pd.DataFrame({
    "workclass": [mappings["workclass"][workclass]],
    "age": [mappings["age"][age]],
    "educational-num": [mappings["educational-num"][education]],
    "marital-status": [mappings["marital-status"][marital]],
    "occupation": [mappings["occupation"][occupation]],
    "hours-per-week": [mappings["hours-per-week"][hours_per_week]],
    "relationship": [mappings["relationship"][relationship]],
    "gender": [mappings["gender"][gender]],
    "race": [mappings["race"][race]],
    "native-country": [mappings["native-country"][country]],
    "capital-gain": [mappings["capital-gain"][capt_gain]],
    "capital-loss": [mappings["capital-loss"][capt_loss]],
    "fnlwgt": [mappings["fnlwgt"][fnlwgt]]
})

st.write("### Input Data")
st.write(input_df)

# Predict button
if st.button("Predict Salary Class"):
    prediction = model.predict(input_df)
    st.success(f"Prediction: {prediction[0]}")
