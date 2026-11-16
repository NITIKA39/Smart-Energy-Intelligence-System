import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Smart Energy Intelligence",
    page_icon="⚡",
    layout="wide"
)

# Load results
results = pd.read_csv("energy_results.csv")
results["timestamp"] = pd.to_datetime(results["timestamp"])

# Separate normal and anomalous readings
# Isolation Forest uses a negative anomaly score for unusual observations.
anomalies = results[results["anomaly_score"] < 0]
normal = results[results["anomaly_score"] >= 0]

# Title
st.title("Smart Energy Intelligence System")
st.caption("AI-powered electricity consumption anomaly detection")

st.divider()

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Readings", len(results))

with col2:
    st.metric("Anomalies Detected", len(anomalies))

with col3:
    anomaly_rate = (len(anomalies) / len(results)) * 100
    st.metric("Anomaly Rate", f"{anomaly_rate:.2f}%")

with col4:
    avg_kwh = results["kwh"].mean()
    st.metric("Average Consumption", f"{avg_kwh:.2f} kWh")

st.divider()

# Consumption chart
st.subheader("Electricity Consumption Monitoring")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    results["timestamp"],
    results["kwh"],
    label="Energy Consumption"
)

ax.scatter(
    anomalies["timestamp"],
    anomalies["kwh"],
    label="Detected Anomaly"
)

ax.set_xlabel("Time")
ax.set_ylabel("Electricity Consumption (kWh)")
ax.set_title("Energy Consumption and Detected Anomalies")
ax.legend()
ax.grid(True, alpha=0.3)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# Anomaly table
st.subheader("Detected Unusual Consumption")

display_data = anomalies[
    ["timestamp", "kwh", "anomaly_score"]
].copy()

display_data.columns = [
    "Timestamp",
    "Consumption (kWh)",
    "Anomaly Score"
]

st.dataframe(
    display_data,
    use_container_width=True,
    hide_index=True
)

# Recommendation
st.subheader("Recommended Action")

st.info(
    "Investigate the flagged time periods for possible avoidable "
    "energy consumption, equipment issues, or unusual operating schedules."
)

st.caption(
    "Note: The dataset used for this prototype is illustrative/sample data."
)