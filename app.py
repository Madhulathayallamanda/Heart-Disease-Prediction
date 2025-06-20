import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

# Load model and data
model = joblib.load("model.pkl")
data = pd.read_csv("heart.csv").drop("target", axis=1)

st.set_page_config(page_title="Heart Disease Predictor", page_icon="💓")
st.title("💓 Heart Disease Prediction")

# Sidebar input
def user_input():
    st.sidebar.header("Enter Patient Data:")
    age = st.sidebar.slider("Age", 18, 100, 50)
    sex = st.sidebar.selectbox("Sex (1=Male, 0=Female)", [1, 0])
    cp = st.sidebar.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
    trestbps = st.sidebar.slider("Resting Blood Pressure", 80, 200, 120)
    chol = st.sidebar.slider("Cholesterol", 100, 400, 200)
    fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120? (1=Yes, 0=No)", [0, 1])
    restecg = st.sidebar.selectbox("Rest ECG (0–2)", [0, 1, 2])
    thalach = st.sidebar.slider("Max Heart Rate Achieved", 70, 210, 150)
    exang = st.sidebar.selectbox("Exercise Induced Angina (1=Yes, 0=No)", [0, 1])
    oldpeak = st.sidebar.slider("ST Depression", 0.0, 6.0, 1.0)
    slope = st.sidebar.selectbox("Slope (0–2)", [0, 1, 2])
    ca = st.sidebar.selectbox("Major Vessels (0–4)", [0, 1, 2, 3, 4])
    thal = st.sidebar.selectbox("Thalassemia (1=Normal, 2=Fixed Defect, 3=Reversible)", [1, 2, 3])

    user_data = {
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }

    return pd.DataFrame([user_data])

input_df = user_input()

# Prediction
prediction = model.predict(input_df)[0]
prediction_proba = model.predict_proba(input_df)[0][prediction]

st.subheader("🩺 Prediction Result:")
if prediction == 1:
    st.error(f"🚨 High Risk of Heart Disease! (Confidence: {prediction_proba:.2f})")
else:
    st.success(f"✅ Low Risk of Heart Disease (Confidence: {prediction_proba:.2f})")

# Save input + prediction to CSV with timestamp
input_df["prediction"] = prediction
input_df["confidence"] = round(prediction_proba, 2)
input_df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if not os.path.exists("user_logs.csv"):
    input_df.to_csv("user_logs.csv", index=False)
else:
    input_df.to_csv("user_logs.csv", mode='a', header=False, index=False)

# Feature Importance (Non-SHAP)
if hasattr(model, "feature_importances_"):
    st.subheader("📊 Feature Importance (Top 5)")
    importances = pd.Series(model.feature_importances_, index=data.columns)
    top_features = importances.sort_values(ascending=False).head(5)
    st.bar_chart(top_features)
else:
    st.info("Feature importance not available for this model.")

# Footer
st.markdown("---")
st.markdown("🧠 *Developed by Yallamanda Madhulatha – CSE 3rd Year*")
