
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
print("Loading data...")
try:
    df = pd.read_csv('merged_data_refined.csv')
    df['Date'] = pd.to_datetime(df['Date'])
except FileNotFoundError:
    print("merged_data_refined.csv not found.")
    raise

# --- Feature Engineering for Trade Profitability Prediction ---
# Target: Will this trade be profitable? (1 if PnL > 0, else 0)
df['Target'] = (df['Closed PnL'] > 0).astype(int)

# Features:
# 1. Sentiment_Value: Fear/Greed index (0-100)
# 2. Size USD: Trade size
# 3. Side: Buy/Sell (needs encoding)
# 4. Fee: Transaction fee (might correlate with complexity/size)
# 5. Hour: Maybe time of day matters (extract from Timestamp if possible, but let's stick to simple ones)

# Encode 'Side'
df['Side_Code'] = df['Side'].astype('category').cat.codes

# Select Features
features = ['Sentiment_Value', 'Size USD', 'Side_Code', 'Fee', 'Start Position']
# Check for NaNs
model_data = df[features + ['Target']].dropna()

print(f"Data ready for modeling. Samples: {len(model_data)}")
print(model_data[features].head())

X = model_data[features]
y = model_data['Target']

# Splitting Data
# Simple random split since dates are sparse and non-contiguous
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
print("Training Random Forest Classifier on Trade Data...")
# Limit depth/estimators for speed given 200k rows
model = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42, n_jobs=-1) 
model.fit(X_train, y_train)

# Evaluation
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

print(f"\n--- Model Results ---")
print(f"Accuracy: {acc:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, preds))

# Feature Importance
importances = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)
print("\nFeature Importance:")
print(importances)

# Plot Feature Importance
plt.figure(figsize=(8, 5))
sns.barplot(x=importances.values, y=importances.index)
plt.title('Feature Importance for Predicting Trade Profitability')
plt.tight_layout()
plt.savefig('feature_importance.png')
print("Feature importance plot saved.")
