import json
import os
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d")

# file name
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
    memos.append({
        "text": memo,
        "date": now
    })
    save_memos(memos)
    print("Memo saved!")

elif choice == "2":
    memos = load_memos()
    print("=== Memo List ===")
    for i, m in enumerate(memos, start=1):
        print(f"{i}. {m['text']}  ({m['date']})")


else:
    print("Invalid option.")
