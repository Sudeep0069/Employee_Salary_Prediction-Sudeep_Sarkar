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
work= {
    "Private":3,
    "Federal-gov":1,
    "State-gov":8
}
edu={
    "HS-grad":9,
    "10th":6,
    "Some-college":10,
    "Masters":14,
    "Bachelors":13
}
mar={
    "Married":2,
    "Unmarried":4,
    "Divorced":0

}
occ={
   "Tech-support":10,
   "Craft-repair":4,
   "others":3
}
gen={
    "Male":1,
    "Female":0
}
rel={
    "Husband":0,
    "Own-child":1,
    "Wife":3
}
rc={
    "White":4,
    "Black":2
}
cont={
    "United-States":0,
    "India":2,
    "Peru":11
}
age= st.sidebar.slider("Age",18,65,25)
workclass= st.sidebar.selectbox("Workclass",[
    "Private","Federal-gov","State-gov"
])
fnlwgt= st.sidebar.selectbox("fnlwgt",[
    116541,236157,158548
])
education= st.sidebar.selectbox("Education Level",[
    "Bachelors","Masters","HS-grad","Some-college","10th"
])
marital= st.sidebar.selectbox("Marital_Status",[
    "Married","Unmarried","Divorced"
])
occupation= st.sidebar.selectbox("occupation",[
    "Tech-support","Craft-repair","others"
])
gender= st.sidebar.selectbox("Gender",[
    "Male","Female"
])
relationship= st.sidebar.selectbox("Relationship",[
    "Husband","Own-child","Wife"
])
race= st.sidebar.selectbox("Race",[
    "White","Black"
])
country= st.sidebar.selectbox("country",[
    "United-States","India","Peru"
])
hours_per_week= st.sidebar.slider("Hours per week",1,80,40)
capt_gain= st.sidebar.slider("Capital Gain",10000,50000,99999)
capt_loss= st.sidebar.slider("Capital Loss",0,1000,2000)
#build input dataframe
input_df= pd.DataFrame({
    'workclass': work[workclass],
    'age': [age],
    'education': edu[education],
    'marital-status': mar[marital],
    'occupation': occ[occupation],
    'hours-per-week': [hours_per_week],
    'relationship': rel[relationship],
    'gender': gen[gender],
    'race': rc[race],
    'country': cont[country],
    'capital-gain': [capt_gain],
    'capital-loss': [capt_loss],
    'fnlwgt': [fnlwgt]
    })

st.write("### Input Data")
st.write(input_df)

#predict button
if st.button("Predict Salary Class"):
  prediction= model.predict(input_df)
  st.success(f"Prediction: {prediction[0]}")
