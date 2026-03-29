

## Bring Your Own Project: Final Report
Project Title: AI-Powered Personal Finance Tracker
## Student Name: Suryansh Singh
## 1. The Problem:
I noticed that manual expense tracking is often abandoned because people don't want to type in
categories. Furthermore, standard apps don't tell you how much you will spend next month.
## 2. Approach:
Data Engineering: I created a synthetic dataset representing student life (small food costs,
monthly bills).
Feature Selection: I used Amount and Vendor ID as features for classification.
Algorithms: I applied Supervised Learning. I chose Random Forest because it is less likely to
overfit on small datasets compared to a deep neural network.
## 3. Challenges & Learning:
Challenge: Converting text (Descriptions) into numbers so the model could process them.
Solution: Used a mapping technique (Label Encoding) to turn "Starbucks" into 1.
Learning: I learned that even simple Linear Regression can be powerful for budgeting if the data
is clean.