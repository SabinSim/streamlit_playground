
# 📝 Sabin's Memo App

Simple CRUD Memo Application (Create + Read)


This project provides simple memo features — **Add Memo / View Memos / Save to JSON** —
implemented in two versions:

* **CLI Version (memo.py)**
* **Streamlit Web Version (memo_streamlit.py)**

---

## 🚀 Features

### ✔ 1. Add Memo 

* Input memo text

* Auto-save with current date (`YYYY-MM-DD`)

* Stored in `memos.json`

### ✔ 2. Show Memo List

* Load and display memos with index + date

### ✔ 3. JSON Storage 

* Data stored in a JSON list

* Automatically creates file if missing

---

## 📂 Project Structure

```
memo-app/
│
├── memo.py                 # Console version
├── memo_streamlit.py       # Streamlit web version
├── memos.json              # Data storage (auto created)
└── README.md
```

---

## 🧩 Code Example — Console Version (CLI)

```python
import json
import os
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d")
FILE_NAME = "memos.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

def load_memos():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_memos(memos):
    with open(FILE_NAME, "w") as f:
        json.dump(memos, f, indent=2)

print("=== Sabin's Memo App ===")
print("1) Add Memo")
print("2) Show Memos")

choice = input("Select option: ")

if choice == "1":
    memo = input("Write memo: ")
    memos = load_memos()
    memos.append({"text": memo, "date": now})
    save_memos(memos)
    print("Memo saved!")

elif choice == "2":
    memos = load_memos()
    print("=== Memo List ===")
    for i, m in enumerate(memos, start=1):
        print(f"{i}. {m['text']}  ({m['date']})")
else:
    print("Invalid option.")
```

---

## 🌐 Code Example — Streamlit Version

```python
import streamlit as st
import json
import os
from datetime import datetime

FILE_NAME = "memos.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

def load_memos():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_memos(memos):
    with open(FILE_NAME, "w") as f:
        json.dump(memos, f, indent=2)

st.title("📝 Sabin's Memo App (Streamlit Version)")

menu = st.radio("Select an option:", ["Add Memo", "Show Memos"])

if menu == "Add Memo":
    text = st.text_input("Write your memo:")
    
    if st.button("Save Memo"):
        if text.strip() == "":
            st.warning("Memo cannot be empty.")
        else:
            now = datetime.now().strftime("%Y-%m-%d")
            memos = load_memos()
            memos.append({"text": text, "date": now})
            save_memos(memos)
            st.success("Memo saved!")

elif menu == "Show Memos":
    memos = load_memos()
    
    if not memos:
        st.info("No memos yet.")
    else:
        st.subheader("📄 Memo List")
        for i, memo in enumerate(memos, start=1):
            st.write(f"**{i}. {memo['text']}**  ({memo['date']})")
```

---

## 📝 How to Run

### ✔ 1) Console Version (CLI)

```bash
python3 memo.py
```

### ✔ 2) Streamlit Version

```bash
pip install streamlit
streamlit run memo_streamlit.py
```

---

## 🔧 Future Improvements 

* Add delete/edit → Full CRUD

* Add category or tag support

* Add search function

* Upgrade to SQLite for persistent DB

* Improve Streamlit UI design

---

## 📜 License

MIT License


