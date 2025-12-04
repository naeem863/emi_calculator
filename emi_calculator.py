import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bike EMI Calculator", layout="wide")

st.title(" Bike EMI Calculator")

bike_prices = {
    "Royal Enfield Hunter 350": 158229,
    "Honda Shine": 85000,
    "Honda SP125": 95000,
    "TVS Apache 160": 118000,
    "Bajaj Pulsar 150": 110000,
    "Royal Enfield Classic 350": 220000,
    "KTM Duke 200": 210000,
    "Yamaha FZ": 120000,
    "Suzuki Gixxer": 135000,
    "Yamaha R15": 180000
}

bike = st.selectbox("Select a Bike", list(bike_prices.keys()))
price = bike_prices[bike]

st.subheader(f" On-road Price: ₹ {price:,}")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Down Payment")

    down_payment = st.slider("Select Down Payment", 0, price, 5000)
    st.write(f"Entered Down Payment: **₹ {down_payment:,}**")

    loan_amount = price - down_payment
    st.markdown(f"### Your Loan Amount Will Be: **₹ {loan_amount:,}**")

    st.markdown("---")

    st.subheader("Tenure & Interest")

    tenure = st.slider("Select Tenure (Months)", 6, 60, 36)

    interest_rate = 10  
    st.write(f"Interest Rate: **{interest_rate}%** (Fixed)")

monthly_interest = interest_rate / (12 * 100)

def calc_emi(P, r, n):
    return (P * r * (1 + r)**n) / ((1 + r)**n - 1)

emi = calc_emi(loan_amount, monthly_interest, tenure)

total_amount = emi * tenure
total_interest = total_amount - loan_amount

with col2:
    st.subheader(f" Monthly EMI: ₹ {emi:,.0f} for {tenure} months")

st.markdown("---")


chart_col, summary_col = st.columns([1.2, 1])

with chart_col:
    st.subheader(" EMI Breakdown")

    labels = ["Principal Loan Amount", "Total Interest Payable"]
    values = [loan_amount, total_interest]
    colors = ["#00A79D", "#FF9A00"]

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
    ax.axis("equal")

    st.pyplot(fig)

with summary_col:
    st.subheader(" Payment Summary")
    st.write(f"**Principal Loan Amount:** ₹ {loan_amount:,}")
    st.write(f"**Total Interest Payable:** ₹ {total_interest:,}")
    st.write(f"**Total Amount Payable:** ₹ {total_amount:,}")
