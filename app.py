import streamlit as st

st.set_page_config(page_title="Yield Analysis", layout="centered")

st.title("AI-Based Package Yield Analysis")
st.write("Simple, public, free yield comparison tool")

st.subheader("Enter Package Components")

total_price = st.number_input("Total Package Price (€)", value=1120.0)
flight = st.number_input("Flight Cost (€)", value=420.0)
hotel = st.number_input("Hotel Net Rate (€)", value=510.0)
transfer = st.number_input("Transfer + Operations (€)", value=70.0)

margin = total_price - (flight + hotel + transfer)

st.subheader("Result")

st.metric("Estimated Gross Margin (€)", round(margin, 2))

if margin < 100:
    st.error("⚠️ High Yield Risk")
elif margin < 150:
    st.warning("⚠️ Medium Yield Risk")
else:
    st.success("✅ Low Yield Risk")

st.caption("Created by Başak Sedef Ustundag")
