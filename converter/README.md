

# 💱 Currency Converter (CHF ↔ EUR)


A simple **Swiss Franc (CHF) ↔ Euro (EUR)** currency converter project.
`converter.py` provides a console version and `converter_streamlit.py` provides a Streamlit web UI version.

---

## 🚀 Features 

### ✔ Console Version (converter.py)

* Convert CHF → EUR

* Convert EUR → CHF

* Simple console-based interface

### ✔ Streamlit Web Version (converter_streamlit.py)

* Clean and intuitive web interface

* Real-time amount input

* Instant conversion results

---

## 📂 Project Structure

```
converter/
│
├── converter.py              # Console version
├── converter_streamlit.py    # Streamlit web version
└── README.md
```

---

## 🧩 Code Example (Console) 

```python
rate = 1.05  # exchange rate

choice = input("Select an option: 1) CHF → EUR | 2) EUR → CHF: ")

if choice == "1":
    print("=== Currency Converter ===")
    amount = float(input("Enter amount in CHF: "))
    result = amount * rate
    print("EUR:", result)

elif choice == "2":
    print("=== Currency Converter ===")
    amount = float(input("Enter amount in EUR: "))
    result = amount / rate
    print("CHF:", result)

else:
    print("Invalid option.")
```

---

## 🌐 Code Example (Streamlit)

```python
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
```

---

## 📝 How to Run 

### ✔ Console Version

```bash
python3 converter.py
```

### ✔ Streamlit Web Version

```bash
pip install streamlit
streamlit run converter_streamlit.py
```

A browser window will open automatically and load the web interface.

---

## 🔧 Future Improvements


* Integrate real-time exchange rate API

* Multi-currency support

* Improve Streamlit UI design + dark mode

* Input validation & error handling

* Show last updated time for exchange rate

---

## 📜 License

MIT License


