import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv('data/transactions.csv')

# 2. ML Part A: Transaction Classification (Categorization)
# We map descriptions to simple IDs for the model to understand
desc_map = {'Starbucks Coffee': 1, 'Uber Ride': 2, 'Amazon Electronics': 3, 'Airtel Wifi Bill': 4, 'McDonalds': 1, 'Zomato Order': 1, 'Petrol Pump': 2, 'Netflix Subscription': 4, 'Grocery Store': 3}
df['Desc_ID'] = df['Description'].map(desc_map)

X_class = df[['Amount', 'Desc_ID']]
y_class = df['Category']

clf = RandomForestClassifier(n_estimators=10)
clf.fit(X_class, y_class)

# Test Classification
test_expense = [[550, 1]] # 550 rupees at a coffee shop (ID 1)
print(f"--- AI Categorization ---")
print(f"Predicted Category for 550 spent at Coffee Shop: {clf.predict(test_expense)[0]}")

# 3. ML Part B: Budget Forecasting (Regression)
# Monthly totals for Jan and Feb
monthly_data = pd.DataFrame({
    'Month_Index': [1, 2],
    'Total_Spent': [6100, 2499] # Example totals from CSV
})

X_reg = monthly_data[['Month_Index']]
y_reg = monthly_data['Total_Spent']

reg = LinearRegression()
reg.fit(X_reg, y_reg)

# Predict Month 3 (March)
march_pred = reg.predict([[3]])
print(f"\n--- AI Budget Forecast ---")
print(f"Predicted Spending for March 2026: ₹{march_pred[0]:.2f}")

# 4. Data Visualization
plt.figure(figsize=(8, 5))
df.groupby('Category')['Amount'].sum().plot(kind='pie', autopct='%1.1%f%%')
plt.title('Spending Distribution by Category')
plt.savefig('spending_chart.png')
print("\nVisualization saved as 'spending_chart.png'")
