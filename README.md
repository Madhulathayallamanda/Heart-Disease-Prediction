# 💓 Heart Disease Prediction App
A machine learning web app using Streamlit that predicts the risk of heart disease from patient input. Trained on the UCI Heart Disease dataset with multiple models, the app selects the best one for predictions.

## 🚀 Features
- Real-time prediction with confidence score
- Sidebar form to enter patient data
- Top 5 feature importance visualization
- User logs saved with timestamp
- Compares Random Forest, Logistic Regression, and Gradient Boosting

## 🔧 Tech Stack
Python, Streamlit, scikit-learn, pandas, joblib, matplotlib

## 📁 Files
- `app.py`: Main Streamlit app
- `model.py`: Trains & saves best model
- `explain_model.py`: Saves feature importance plot
- `heart.csv`: Dataset
- `model.pkl`: Trained model
- `feature_importance.png`: Plot image
- `user_logs.csv`: Logs of predictions
- `requirements.txt`: Python dependencies

## ▶️ Run Locally
```bash
pip install -r requirements.txt
python model.py
streamlit run app.py

## 📤 Deploy
You can deploy this project on [Streamlit Cloud](https://share.streamlit.io/) by uploading all files in this repository.  
Steps:
1. Go to Streamlit Cloud and sign in.
2. Click **"New App"**.
3. Connect your GitHub repo.
4. Set the main file as `app.py`.
5. Click **"Deploy"**.

## 🙋‍♀️ Author
**Yallamanda Madhulatha**  
CSE 3rd Year  
📧 your-email@example.com  
🔗 [LinkedIn](https://linkedin.com/in/your-profile)

## 📄 License
This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute with attribution.

