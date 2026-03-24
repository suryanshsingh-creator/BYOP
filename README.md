# 💰 Smart Finance Tracker (AI/ML BYOP)

## 📌 Problem Statement
Managing student finances is difficult. This project uses **Machine Learning** to automate the process of categorizing expenses and forecasting future monthly budgets to prevent overspending.

## 🤖 AI/ML Implementation
- **Classification**: A `RandomForestClassifier` identifies the category (Food, Bills, etc.) based on the amount and vendor.
- **Regression**: A `LinearRegression` model analyzes monthly trends to predict next month's total expenditure.

## 🛠️ Setup
1. Install requirements: `pip install -r requirements.txt`
2. Clone the Repository:
`git clone [https://github.com/suryanshsingh-creator/BYOP]`
3. Install Dependencies: `pip install -r requirements.txt`
4. Run the main script: `python main.py`

##🧠 Machine Learning Methodology
Model,Purpose,Fundamental AI/ML Concept
Random Forest,Categorization,"Classification: Mapping inputs to discrete labels (e.g., Food vs. Transport)."
Linear Regression,Forecasting,"Regression: Predicting a continuous numerical value (e.g., ₹ Total Amount)."

📂 Repository Structure
main.py: The primary script containing the ML models and execution logic.

data/transactions.csv: The dataset used for training and testing the models.

requirements.txt: List of necessary Python libraries for the environment.

spending_chart.png: Visual output generated automatically after running the script.

README.md: This comprehensive project documentation.

## 📊 Results
- **Auto-Categorization**: Successfully identifies recurring vendors.
- **Visuals**: Generates a `spending_chart.png` to show a breakdown of expenses.
