# AI Telco Customer Churn Analysis

AI-powered Telco Customer Churn Analysis using Python, Machine Learning and Power BI.

## 📌 Project Overview

This project analyzes customer churn data and uses Machine Learning to predict customers who are at higher risk of churn.

The project combines:

- Python for data cleaning and feature engineering
- Machine Learning for churn prediction
- Automated prediction pipeline
- Power BI for interactive business reporting
- AI-based customer risk segmentation

## 🎯 Business Problem

Customer churn can negatively impact revenue and customer retention.

The objective of this project is to:

- Identify important churn patterns
- Predict the probability of customer churn
- Segment customers into Low, Medium and High Risk
- Help business teams prioritize retention activities
- Present actionable insights through Power BI

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Excel
- Power BI
- DAX
- Machine Learning
- Random Forest
- Logistic Regression

## 🔄 Project Workflow

Raw Customer Data
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Exploratory & Business Analysis
        ↓
Machine Learning
        ↓
Model Comparison
        ↓
Random Forest Selection
        ↓
Churn Probability Prediction
        ↓
AI Risk Segmentation
        ↓
Automated Prediction Pipeline
        ↓
Power BI Dashboard

## 📊 Dataset

The dataset contains 7,043 customer records.

Key information includes:

- Customer demographics
- Tenure
- Contract information
- Internet services
- Monthly charges
- Total charges
- Support tickets
- Services used
- Customer churn status

Additional engineered features include:

- TotalTickets
- TenureGroup
- MonthlyChargeGroup
- TotalServices
- CustomerValueGroup
- RiskScore
- ChurnRiskSegment

## 🤖 Machine Learning

Two classification models were developed and compared:

1. Logistic Regression
2. Random Forest Classifier

### Model Performance

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 85.66% | 75.44% | 68.18% | 71.63% | 92.75% |
| Random Forest | 84.88% | 69.03% | 78.07% | 73.27% | 91.34% |

Random Forest was selected based on the project objective of identifying customers at risk of churn, with particular focus on recall and F1 score.

## 🧠 AI Risk Segmentation

The Random Forest model generates a churn probability for every customer.

Risk levels are assigned using the following thresholds:

- Low Risk: Churn probability < 30%
- Medium Risk: 30%–59%
- High Risk: ≥ 60%

### AI Risk Distribution

- Low Risk: 4,564 customers
- Medium Risk: 633 customers
- High Risk: 1,846 customers

Average predicted churn probability is approximately 32%.

## 📈 Power BI Dashboard

The Power BI dashboard contains three pages:

### Page 1 — Churn Overview

Provides an overall view of:

- Customer churn rate
- Churn by contract
- Churn by tenure
- Customer distribution
- Key churn patterns

### Page 2 — Customer & Churn Analysis

Focuses on:

- Customer segments
- Customer value
- Internet services
- Monthly charges
- Support tickets
- Churn patterns across customer groups

### Page 3 — AI-Powered Customer Churn Prediction

Provides:

- AI Risk Distribution
- AI High-Risk Customers
- Average Churn Probability
- AI Risk Level vs Actual Churn
- Churn Probability by Contract
- High-Risk Customer Details
- Random Forest Model Performance
- Key Business Insights

## ⚙️ Automation

An automated Python pipeline was created to generate customer churn predictions.

The pipeline:

1. Loads the processed customer dataset
2. Loads the trained Random Forest model
3. Generates churn predictions
4. Calculates churn probabilities
5. Assigns AI risk levels
6. Exports the results to Excel

Main automation script:

`scripts/automated_pipeline.py`

## 📁 Project Structure

```text
AI-Telco-Customer-Churn-Analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── customer_churn_final.xlsx
│       └── ai_churn_predictions_automated.xlsx
│
├── models/
│   └── churn_random_forest_model.pkl
│
├── notebooks/
│
├── scripts/
│   └── automated_pipeline.py
│
├── powerbi/
│   └── AI_Telco_Customer_Churn_Dashboard.pbix
│
├── screenshots/
│
├── requirements.txt
└── README.md