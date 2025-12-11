import streamlit as st
import pandas as pd
import joblib

st.title("YouTube Revenue Prediction App")

# Load saved model only
model = joblib.load("best_youtube_model.joblib")

st.subheader("Enter Video Details")

# User Inputs
views = st.number_input("Views", min_value=0)
likes = st.number_input("Likes", min_value=0)
comments = st.number_input("Comments", min_value=0)
subscribers = st.number_input("Subscribers", min_value=0)
engagement_rate = st.number_input("Engagement Rate", min_value=0.0)
watch_per_view = st.number_input("Watch Time Per View (min)", min_value=0.0)

category = st.selectbox("Category", ["Education", "Gaming", "Tech", "Food", "Music", "Other"])
device = st.selectbox("Device", ["Mobile", "Desktop", "Tablet", "TV"])
country = st.selectbox("Country", ["IN", "US", "UK", "CA", "AU", "Others"])

if st.button("Predict Revenue"):
    
    # Prepare input dataframe
    input_df = pd.DataFrame({
        "views":[views],
        "likes":[likes],
        "comments":[comments],
        "subscribers":[subscribers],
        "engagement_rate":[engagement_rate],
        "watch_per_view":[watch_per_view],
        "category":[category],
        "device":[device],
        "country":[country]
    })

    # USD prediction (model always gives USD)
    pred_usd = model.predict(input_df)[0]

    # Currency conversion
    if country == "IN":
        conversion_rate = 83   # 1 USD ≈ 83 INR (example)
        pred_value = pred_usd * conversion_rate
        currency_symbol = "₹"
        currency_name = "INR"
    else:
        pred_value = pred_usd
        currency_symbol = "$"
        currency_name = "USD"

    st.success(f"✅ Predicted Ad Revenue: **{currency_symbol}{pred_value:.2f} {currency_name}**")

