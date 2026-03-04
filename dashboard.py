import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px

st.title("Real-Time Fraud Monitoring Dashboard")

# Connect to Postgres
conn = psycopg2.connect(
    host="localhost",
    database="fraud_db",
    user="fraud",
    password="fraud",
    port=5432
)

query = "SELECT * FROM fraud_predictions"
df = pd.read_sql(query, conn)

# ---- KPI Section ----
st.subheader("Key Metrics")

total_tx = len(df)
fraud_count = df["fraud_label"].sum()
fraud_rate = (fraud_count / total_tx) * 100 if total_tx > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions", total_tx)
col2.metric("Fraud Transactions", int(fraud_count))
col3.metric("Fraud Rate (%)", f"{fraud_rate:.2f}%")

# ---- Line Chart ----
st.subheader("Transactions Over Time")

df["event_time"] = pd.to_datetime(df["event_time"])
tx_time = df.groupby(df["event_time"].dt.floor("T")).size().reset_index(name="count")

fig = px.line(tx_time, x="event_time", y="count")
st.plotly_chart(fig)

# ---- Fraud Score Distribution ----
st.subheader("Fraud Score Distribution")
fig2 = px.histogram(df, x="fraud_score", nbins=20)
st.plotly_chart(fig2)

# ---- Latest Transactions ----
st.subheader("Latest Transactions")
st.dataframe(df.sort_values("event_time", ascending=False).head(20))