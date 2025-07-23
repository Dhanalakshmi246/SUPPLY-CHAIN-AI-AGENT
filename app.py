import streamlit as st
import pandas as pd
from agents import InventoryAgent, SalesAgent, LogisticsAgent

st.title("🧠 Multi-Agent Supply Chain Optimizer")

uploaded_file = st.file_uploader("📂 Upload Supply Chain CSV", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    st.subheader("📊 Uploaded Data")
    st.dataframe(data)

    inventory_agent = InventoryAgent(data)
    sales_agent = SalesAgent(data)
    logistics_agent = LogisticsAgent(data)

    if st.button("🔁 Reorder Check"):
        st.subheader("📦 Products Needing Reorder")
        st.dataframe(inventory_agent.check_reorder())
    if st.button("📈 Top Sales"):
        st.subheader("🔥 Top Selling Products")
        st.dataframe(sales_agent.analyze_sales())

    if st.button("🚛 Delivery Priority"):
        st.subheader("🚚 Prioritize Based on Lead Time")
        st.dataframe(logistics_agent.calculate_delivery_priority())
