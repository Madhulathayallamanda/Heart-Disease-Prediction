# 🫀 Heart Disease Prediction using Machine Learning

This project uses various machine learning algorithms to predict whether a patient is likely to have heart disease based on medical attributes. The goal is to assist healthcare professionals by providing a second opinion based on data analysis.

## 📊 Dataset

The dataset used is from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/heart+Disease). It includes 303 patient records with 14 attributes such as age, sex, cholesterol level, resting blood pressure, etc.

## 🧠 Algorithms Used

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest

## 🔍 Exploratory Data Analysis

- Null values handled
- Correlation heatmap
- Target class distribution
- Pairplots for feature relationships

## 📈 Model Evaluation

| Model              | Accuracy Score |
|-------------------|----------------|
| Logistic Regression | 86.89%        |
| K-Nearest Neighbors | 83.60%        |
| Support Vector Machine | 85.25%     |
| Decision Tree       | 81.96%        |
| Random Forest       | 88.52% ✅      |

✅ **Random Forest performed best** on the dataset.

## 🌐 Live Web App (Streamlit)

We have also deployed this project as a simple web app using Streamlit.

👉 [Click here to try the live app](#) *(Coming soon)*

Or run locally:

```bash
streamlit run streamlit_app.py

⚙️ How to Run Locally
# Clone the repo
git clone https://github.com/Madhulathayallamanda/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py

🗂️ Project Structure
Heart-Disease-Prediction/
├── heart.csv
├── model_training.ipynb
├── streamlit_app.py
├── requirements.txt
└── README.md

✅ Requirements
pip install -r requirements.txt

🧪 Tech Stack
Python
Scikit-learn
Pandas, NumPy
Matplotlib, Seaborn
Streamlit (for web app)

📬 Contact
Madhulatha Yallamanda
📧madhulathayallamanda@gmail.com

