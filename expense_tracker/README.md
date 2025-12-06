# 💰 Sabin's Expense Tracker

Simple personal finance tracking app with SQLite & Streamlit.

This project is an **Expense Tracker** that allows users to add spending records, view lists, delete items, and see summaries (monthly & category-based).
It includes two implementations:

* **CLI Version (Python + SQLite)**
* **Streamlit Web Version (Interactive UI)**

Everything is stored locally using **SQLite**, and Streamlit provides a clean UI with tables and charts.

---

## 🚀 Features

### ✔ Add Expense

* Enter amount (CHF), category, note
* Auto-save date (`YYYY-MM-DD`)
* Stored in SQLite database

### ✔ Show Expense List

* Clean tabular output
* Sorted by latest date

### ✔ Delete Expense

* Select record by ID
* Safe deletion with preview (Streamlit)

### ✔ Monthly Summary

* Group by month
* Total CHF per month
* Display as table + bar chart

### ✔ Category Summary

* Group by category
* Total spending per category
* Table + bar chart visualization

### ✔ SQLite Database

* Local DB file (`expenses.db`)
* Auto-created table
* Persistent storage

### ✔ Streamlit UI

* Sidebar menu navigation
* Clean tables
* Charts for summaries

---

## 📂 Project Structure

```
expense-tracker/
│
├── expense.py                # CLI version
├── expense_streamlit.py      # Streamlit version
├── expenses.db               # SQLite database (auto created)
└── README.md
```

---

# 🧩 Code Examples

---

## 1) CLI Version (expense.py)

```python
import sqlite3
from datetime import datetime

# Add new expense
def add_expense():
    amount = float(input("Amount (CHF): "))
    category = input("Category (Food, Transport, Baby, etc): ")
    note = input("Note: ")
    date = datetime.now().strftime("%Y-%m-%d")

    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO expenses (amount, category, note, date) VALUES (?, ?, ?, ?)",
        (amount, category, note, date),
    )

    conn.commit()
    conn.close()

    print("Expense saved!")

# Show all expenses
def show_expenses():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()

    cur.execute("SELECT id, amount, category, note, date FROM expenses ORDER BY date DESC")
    rows = cur.fetchall()

    conn.close()

    print("\n=== Expense List ===")
    if not rows:
        print("No expenses recorded.")
        return

    for r in rows:
        print(f"{r[0]}. {r[4]} | {r[1]} CHF | {r[2]} | {r[3]}")

# Delete an expense
def delete_expense():
    show_expenses()
    delete_id = input("Enter ID to delete: ")

    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM expenses WHERE id = ?", (delete_id,))
    conn.commit()
    conn.close()

    print("Deleted!")

# Monthly summary
def show_monthly_summary():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT SUBSTR(date, 1, 7) AS month, SUM(amount)
        FROM expenses
        GROUP BY month
        ORDER BY month DESC
    """)

    rows = cur.fetchall()
    conn.close()

    print("\n=== Monthly Summary ===")
    if not rows:
        print("No data.")
        return

    for r in rows:
        print(f"{r[0]} : {r[1]} CHF")

# Category summary
def show_category_summary():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        ORDER BY SUM(amount) DESC
    """)

    rows = cur.fetchall()
    conn.close()

    print("\n=== Category Summary ===")
    if not rows:
        print("No data.")
        return

    for r in rows:
        print(f"{r[0]} : {r[1]} CHF")

# Main menu
def main():
    print("=== Expense Tracker ===")
    print("1) Add Expense")
    print("2) Show Expenses")
    print("3) Monthly Summary")
    print("4) Category Summary")
    print("5) Delete Expense")
    print("6) Exit")

    choice = input("Select option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        show_monthly_summary()
    elif choice == "4":
        show_category_summary()
    elif choice == "5":
        delete_expense()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
```

---

## 2) Streamlit Version (expense_streamlit.py)

```python
import streamlit as st
import sqlite3
from datetime import datetime
import pandas as pd

DB = "expenses.db"

# Load data from database
def get_data():
    conn = sqlite3.connect(DB)
    df = pd.read_sql_query("SELECT * FROM expenses ORDER BY date DESC", conn)
    conn.close()
    return df

# Add new expense
def add_expense(amount, category, note):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d")
    cur.execute(
        "INSERT INTO expenses (amount, category, note, date) VALUES (?, ?, ?, ?)",
        (amount, category, note, date),
    )
    conn.commit()
    conn.close()

st.title("💰 Sabin's Expense Tracker")

menu = st.sidebar.radio("Menu", [
    "Add Expense",
    "Show Expenses",
    "Monthly Summary",
    "Category Summary",
    "Delete Expense"
])

# Monthly summary from DB
def get_monthly_summary():
    conn = sqlite3.connect(DB)
    df = pd.read_sql_query("""
        SELECT SUBSTR(date, 1, 7) AS month, SUM(amount) AS total
        FROM expenses
        GROUP BY month
        ORDER BY month DESC
    """, conn)
    conn.close()
    return df

# Category summary from DB
def get_category_summary():
    conn = sqlite3.connect(DB)
    df = pd.read_sql_query("""
        SELECT category, SUM(amount) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
    """, conn)
    conn.close()
    return df


# Add Expense Page
if menu == "Add Expense":
    st.subheader("Add New Expense")

    amount = st.number_input("Amount (CHF)", min_value=0.0, format="%.2f")
    category = st.text_input("Category")
    note = st.text_area("Note")

    if st.button("Save"):
        if amount == 0 or category.strip() == "":
            st.warning("Amount and category required.")
        else:
            add_expense(amount, category, note)
            st.success("Expense saved!")

# Show Expenses Page
elif menu == "Show Expenses":
    st.subheader("Expense List")
    df = get_data()

    if df.empty:
        st.info("No expenses found.")
    else:
        st.dataframe(df)

# Monthly Summary Page
elif menu == "Monthly Summary":
    st.subheader("📅 Monthly Summary")
    df = get_monthly_summary()

    if df.empty:
        st.info("No data.")
    else:
        st.dataframe(df)
        st.bar_chart(df.set_index("month")["total"])

# Category Summary Page
elif menu == "Category Summary":
    st.subheader("📊 Category Summary")
    df = get_category_summary()

    if df.empty:
        st.info("No data.")
    else:
        st.dataframe(df)
        st.bar_chart(df.set_index("category")["total"])

# Delete Expense Page
elif menu == "Delete Expense":
    st.subheader("🗑 Delete Expense")

    df = get_data()

    if df.empty:
        st.info("No expenses to delete.")
    else:
        delete_id = st.selectbox(
            "Select Expense ID to delete:",
            df["id"]
        )

        selected_row = df[df["id"] == delete_id].iloc[0]
        st.write(f"**Amount:** {selected_row['amount']} CHF")
        st.write(f"**Category:** {selected_row['category']}")
        st.write(f"**Note:** {selected_row['note']}")
        st.write(f"**Date:** {selected_row['date']}")

        if st.button("Delete"):
            conn = sqlite3.connect(DB)
            cur = conn.cursor()
            cur.execute("DELETE FROM expenses WHERE id = ?", (delete_id,))
            conn.commit()
            conn.close()
            st.success("Expense deleted!")
```

---

# 📝 How to Run

## ✔ CLI Version

```
python3 expense.py
```

## ✔ Streamlit Version

```
pip install streamlit pandas
streamlit run expense_streamlit.py
```

---

# 🔧 Future Improvements

* Add editing feature (Update)
* Add filtering by date range
* Add charts for category trends
* Add login system for personal accounts
* Export to CSV / Excel

---

# 📜 License

MIT License

