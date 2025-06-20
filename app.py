# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("heart.csv")
X = df.drop("target", axis=1)
y = df["target"]

model = RandomForestClassifier()
model.fit(X, y)

st.title("🫀 Heart Disease Prediction App")

age = st.slider("Age", 29, 77, 55)
sex = st.radio("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.number_input("Resting BP", 90, 200, 120)
chol = st.number_input("Cholesterol", 100, 600, 250)
fbs = st.radio("Fasting Blood Sugar > 120?", [0, 1])
restecg = st.selectbox("Resting ECG", [0, 1, 2])
thalach = st.number_input("Max Heart Rate", 70, 210, 150)
exang = st.radio("Exercise Induced Angina", [0, 1])
oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of Peak", [0, 1, 2])
ca = st.selectbox("Major Vessels Colored", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                        thalach, exang, oldpeak, slope, ca, thal]])
prediction = model.predict(input_data)

if st.button("Predict"):
    result = "🟢 No Heart Disease" if prediction[0] == 0 else "🔴 High Risk of Heart Disease"
    st.subheader(result)
