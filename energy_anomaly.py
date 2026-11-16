import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("data/energy_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

model = IsolationForest(n_estimators=150, contamination=0.02, random_state=42)
df["prediction"] = model.fit_predict(df[["kwh"]])
df["anomaly"] = df["prediction"].map({1: "Normal", -1: "Anomaly"})
df["anomaly_score"] = model.decision_function(df[["kwh"]])

anomalies = df[df["anomaly"] == "Anomaly"]

print("\nSMART ENERGY INTELLIGENCE SYSTEM")
print("-" * 45)
print(f"Total readings: {len(df)}")
print(f"Anomalies detected: {len(anomalies)}")

if len(anomalies):
    print("\nDetected unusual consumption:")
    print(anomalies[["timestamp", "kwh", "anomaly_score"]].to_string(index=False))
    print("\nAction: Investigate the flagged time periods for possible avoidable consumption.")

df.to_csv("energy_results.csv", index=False)
print("\nResults saved to energy_results.csv")
