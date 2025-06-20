# 💓 Heart Disease Prediction App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR-APP-URL)

A Streamlit-based machine learning web app that predicts the risk of heart disease based on patient health data. It uses the UCI Heart Disease dataset and selects the best-performing model for real-time prediction.

## 🚀 Features
- Predicts heart disease risk based on 13 patient attributes
- Uses the best model out of Random Forest, Logistic Regression, and Gradient Boosting
- Displays top 5 feature importances
- Sidebar form for interactive input
- Saves input + prediction logs with timestamp to `user_logs.csv`

## 🧠 ML Models Used
- ✅ Random Forest (best accuracy)
- Logistic Regression
- Gradient Boosting

## 🔧 Tech Stack
- Python
- Streamlit
- scikit-learn
- pandas
- joblib
- matplotlib

## 📁 Project Structure
heart-disease-predictor/
├── app.py # Streamlit frontend
├── model.py # Trains and saves best model
├── explain_model.py # Feature importance plot
├── heart.csv # Dataset (UCI Heart Disease)
├── requirements.txt # Dependencies
├── README.md # This file

## ▶️ Run Locally
```bash
git clone https://github.com/Madhulathayallamanda/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
pip install -r requirements.txt
python model.py        # Train and save the best model
streamlit run app.py   # Launch the app

📤 Deploy on Streamlit
Go to Streamlit Cloud
Click New App
Select: Madhulathayallamanda/Heart-Disease-Prediction
Set the main file to app.py
Click Deploy
Your app will be live at:
🔗 https://madhulathayallamanda-heart-disease-prediction.streamlit.app

🙋‍♀️ Author
Yallamanda Madhulatha
CSE 3rd Year, Anurag University
📧 madhulathayallamanda@gmail.com

📄 License
This project is licensed under the MIT License – free to use, modify, and distribute with attribution.


