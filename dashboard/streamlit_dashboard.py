import pandas as pd
import streamlit as st
import time

# Page settings
st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")
st.title("🕵️ Real-Time Fraud Detection Dashboard")

# File path (must match where your fraud stream writes to)
csv_path = "/home/mariachmite/suspicious_output.csv"


# Sidebar filters
st.sidebar.header("🔍 Filter Suspicious Transactions")

# Keep refreshing the data every few seconds
REFRESH_EVERY_SECONDS = 5

@st.cache_data(ttl=REFRESH_EVERY_SECONDS)
def load_data():
    try:
        df = pd.read_csv(csv_path, names=["transaction_id", "name", "amount", "location", "timestamp"])
        return df
    except Exception as e:
        st.warning("No suspicious transactions yet...")
        return pd.DataFrame(columns=["transaction_id", "name", "amount", "location", "timestamp"])

df = load_data()
st.write("📂 Data loaded:", df.shape)
st.dataframe(df)

if not df.empty:
    # Filters
    names = st.sidebar.multiselect("Filter by Name", options=df["name"].unique(), default=df["name"].unique())
    locations = st.sidebar.multiselect("Filter by Location", options=df["location"].unique(), default=df["location"].unique())
    min_amount, max_amount = st.sidebar.slider("Amount Range", float(df.amount.min()), float(df.amount.max()), (float(df.amount.min()), float(df.amount.max())))

    # Apply filters
    filtered_df = df[
        (df["name"].isin(names)) &
        (df["location"].isin(locations)) &
        (df["amount"] >= min_amount) &
        (df["amount"] <= max_amount)
    ]

    st.metric("📊 Total Suspicious Transactions", len(filtered_df))
    st.dataframe(filtered_df.sort_values("timestamp", ascending=False), use_container_width=True)
else:
    st.info("Waiting for suspicious transactions to appear...")

st.write(df.head())

