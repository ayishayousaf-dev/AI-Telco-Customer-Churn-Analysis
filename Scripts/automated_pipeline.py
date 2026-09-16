import pandas as pd
import numpy as np
import joblib

input_file = "C:/Users/Lenovo/customer_churn_final.xlsx"
model_file = "C:/Users/Lenovo/churn_random_forest_model.pkl"
output_file = "C:/Users/Lenovo/ai_churn_predictions_automated.xlsx"

print("Starting AI churn prediction pipeline...")

df = pd.read_excel(input_file)
print(f"Data loaded successfully: {df.shape}")

features = [
    "gender", "SeniorCitizen", "Partner", "Dependents", "tenure",
    "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity",
    "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV",
    "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod",
    "MonthlyCharges", "TotalCharges", "numAdminTickets", "numTechTickets",
    "TotalTickets", "TotalServices"
]

model = joblib.load(model_file)
print("AI model loaded successfully!")

predictions = model.predict(df[features])
probabilities = model.predict_proba(df[features])[:, 1]

risk_level = np.where(
    probabilities < 0.30,
    "Low Risk",
    np.where(probabilities < 0.60, "Medium Risk", "High Risk")
)

ai_results = pd.DataFrame({
    "customerID": df["customerID"],
    "ActualChurn": df["Churn"],
    "ChurnProbability": probabilities,
    "PredictedChurn": predictions,
    "AIRiskLevel": risk_level
})

ai_results.to_excel(output_file, index=False)

print("AI predictions generated successfully!")
print(f"Output saved to: {output_file}")
print("Risk distribution:")
print(ai_results["AIRiskLevel"].value_counts())
