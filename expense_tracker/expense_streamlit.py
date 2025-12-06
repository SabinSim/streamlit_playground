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
