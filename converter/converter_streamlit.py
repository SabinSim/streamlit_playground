import streamlit as st

st.title("💱 Currency Converter (CHF ↔ EUR)")

rate = 1.05  # exchange rate

option = st.radio(
    "Select conversion direction:",
    ("CHF → EUR", "EUR → CHF")
)

amount = st.number_input("Enter amount:", min_value=0.0, format="%.2f")

if st.button("Convert"):
    if option == "CHF → EUR":
        result = amount * rate
        st.success(f"{amount} CHF = {result:.2f} EUR")
    else:
        result = amount / rate
        st.success(f"{amount} EUR = {result:.2f} CHF")
