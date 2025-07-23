import streamlit as st
import pandas as pd
import joblib

#load the model
model= joblib.load("best_model.pkl")
st.set_page_config(page_title="Employee Salary Prediction", page_icon="🪙", layout="centered")
st.title("🪙 Employee Salary Prediction App")
st.markdown("predict if you earn >50k or <=50k:")
#sidebar inputs
st.sidebar.header("Input Employee Details")
#replace the fields with your dataset's actual input columns
age= st.sidebar.slider("Age",18,65,25)
gender= st.sidebar.selectbox("Gender",[
    "Male","Female"
])
education= st.sidebar.selectbox("Education Level",[
    "Bachelors","Masters","Doctorate","Assoc-voc","HS-grad","Some-college","10th"
])
occupation= st.sidebar.selectbox("Job Role",[
    "Tech-support","Craft-reapair","Sales","Adm-clerical","Exec-managerial","others"
])
hours_per_week= st.sidebar.slider("Hours per week",1,80,40)
experience= st.sidebar.slider("Years of Experience",0,40,5)
#build input dataframe
input_df= pd.DataFrame({
    'age': [age],
    'education': [education],
    'occupation': [occupation],
    'hours-per-week': [hours_per_week],
    'experience': [experience],
    'gender': [gender]
})

st.write("### Input Data")
st.write(input_df)

#predict button
if st.button("Predict Salary Class"):
  prediction= model.predict(input_df)
  st.success(f"Prediction: {prediction[0]}")
