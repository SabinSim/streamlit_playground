import streamlit as st
import json
import os
from datetime import datetime

FILE_NAME = "memos.json"

# 파일이 없으면 기본 구조 생성
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
