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
