import streamlit as st
import joblib


# Load the trained model
model = joblib.load("customer_segmentation_model.pkl")


# Application title
st.title("Customer Segmentation App")

st.write("Enter customer details to predict the customer segment.")


# Input 1: Annual Income
income = st.number_input(
    "Annual Income (₹)",
    min_value=0,
    max_value=3000000,
    value=500000
)


# Input 2: Monthly Spending
spending = st.number_input(
    "Monthly Spending (₹)",
    min_value=0,
    max_value=100000,
    value=10000
)


# Input 3: Visits per Month
visits = st.number_input(
    "Visits Per Month",
    min_value=0,
    max_value=30,
    value=5
)


# Prediction button
if st.button("Predict Customer Segment"):

    # Check input limits
    if income < 300000 or income > 2000000:
        st.error("Please enter Annual Income between ₹3,00,000 and ₹20,00,000.")

    elif spending < 5000 or spending > 50000:
        st.error("Please enter Monthly Spending between ₹5,000 and ₹50,000.")

    elif visits < 1 or visits > 13:
        st.error("Please enter Visits Per Month between 1 and 13.")

    else:
        # Create input for the model
        new_customer = [[income, spending, visits]]

        # Predict cluster
        prediction = model.predict(new_customer)

        # Display result
        st.success("Customer belongs to Cluster " + str(prediction[0]))
