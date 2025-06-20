
---

## ✅ Step 2: `streamlit_app.py`

Here’s a **simple Streamlit UI** to input user values and predict:

```python
import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sklearn.ensemble import RandomForestClassifier

# Load dataset and train model (can also load pre-trained model)
df = pd.read_csv("heart.csv")
X = df.drop("target", axis=1)
y = df["target"]

model = RandomForestClassifier()
model.fit(X, y)

st.title("🫀 Heart Disease Prediction App")

st.write("Enter the details below to predict heart disease:")

# Input form
age = st.slider("Age", 29, 77, 55)
sex = st.radio("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", 90, 200, 120)
chol = st.number_input("Serum Cholestoral (chol)", 100, 600, 250)
fbs = st.radio("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG Results (restecg)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate (thalach)", 70, 210, 150)
exang = st.radio("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.slider("ST Depression (oldpeak)", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of Peak Exercise ST (slope)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

# Make prediction
input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                        thalach, exang, oldpeak, slope, ca, thal]])
prediction = model.predict(input_data)

if st.button("Predict"):
    result = "🟢 No Heart Disease Detected" if prediction[0] == 0 else "🔴 High Risk of Heart Disease"
    st.subheader(result)
