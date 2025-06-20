# 💓 Heart Disease Prediction App
A machine learning web app built with Streamlit that predicts the risk of heart disease based on patient input. The model is trained using the UCI Heart Disease dataset and compares multiple algorithms to select the best performer.

## 🚀 Features
- Real-time prediction with confidence score
- Sidebar form for interactive input
- Visual display of top 5 feature importances
- Saves prediction logs with timestamp
- Compares Random Forest, Logistic Regression, and Gradient Boosting

## 🔧 Tech Stack
Python, Streamlit, scikit-learn, pandas, joblib, matplotlib

## 📁 File Structure
- `app.py`: Streamlit web application
- `model.py`: Trains and selects the best ML model
- `explain_model.py`: Generates feature importance plot
- `heart.csv`: Input dataset (UCI Heart Disease)
- `requirements.txt`: Required Python packages
- `README.md`: Project overview and usage guide

## ▶️ How to Run Locally
```bash
pip install -r requirements.txt
python model.py
streamlit run app.py

📤 Deploy | 🙋‍♀️ Author | 📄 License
Deploy on Streamlit Cloud → use app.py as the main file.
Author: Yallamanda Madhulatha – CSE 3rd Year
📧 madhulathayallamanda@gmail.com | 🔗 LinkedIn


### ✅ Ready to Deploy on Streamlit Cloud?
Go to [https://share.streamlit.io](https://share.streamlit.io), log in with GitHub, and:
1. Click **“New App”**
2. Select this repo: `Madhulathayallamanda/Heart-Disease-Prediction`
3. Set main file: `app.py`
4. Click **Deploy**

