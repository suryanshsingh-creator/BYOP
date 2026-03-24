# 💰 Smart Finance Tracker (AI/ML BYOP)

## 📌 Problem Statement
Managing student finances is difficult. This project uses **Machine Learning** to automate the process of categorizing expenses and forecasting future monthly budgets to prevent overspending.

## 🤖 AI/ML Implementation
- **Classification**: A `RandomForestClassifier` identifies the category (Food, Bills, etc.) based on the amount and vendor.
- **Regression**: A `LinearRegression` model analyzes monthly trends to predict next month's total expenditure.

## 🛠️ Setup
1. Install requirements: `pip install -r requirements.txt`
2. Run the main script: `python main.py`

## 📊 Results
- **Auto-Categorization**: Successfully identifies recurring vendors.
- **Visuals**: Generates a `spending_chart.png` to show a breakdown of expenses.
