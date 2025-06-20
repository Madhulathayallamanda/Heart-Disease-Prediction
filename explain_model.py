import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

# Load the trained model and data
model = joblib.load("model.pkl")
data = pd.read_csv("heart.csv")
X = data.drop("target", axis=1)

# Get feature importances
importances = model.feature_importances_
feature_names = X.columns
indices = np.argsort(importances)[::-1]

# Plot
plt.figure(figsize=(10, 6))
plt.title("Feature Importances (Random Forest)")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), feature_names[indices], rotation=45)
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.show()
