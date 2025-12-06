

# 🎬 Sabin's Movie Search App

Simple API-based Movie Search (OMDb API)

This project uses the OMDb (Open Movie Database) API to fetch and display movie information.
It includes two versions:

* **CLI Version (movie.py)**
* **Streamlit Web Version (movie_streamlit.py)**

---

## 🚀 Features

### ✔ 1. Movie Search

Search movies by title

* Poster
* Genre
* Ratings
* Plot and more

### ✔ 2. API Request

Using OMDb API

* Fetch data via HTTP request
* Parse JSON results

### ✔ 3. Streamlit UI Version

Streamlit Version supports:

* Clean UI
* Auto poster preview
* Error handling

---

## 📂 Project Structure 

```
movie-app/
│
├── movie.py                 # Console version
├── movie_streamlit.py       # Streamlit version
└── README.md
```

---

# 🧩 Code Example — CLI Version (movie.py)

```python
import requests

API_KEY = "YOUR_API_KEY"  # Put your OMDb API key here

title = input("Movie title: ")

url = f"https://www.omdbapi.com/?t={title}&apikey={API_KEY}"
response = requests.get(url)

if response.status_code != 200:
    print("Error fetching data.")
    exit()

data = response.json()

if data["Response"] == "False":
    print("Movie not found.")
    exit()

print("=== Movie Info ===")
print("Title:", data["Title"])
print("Year:", data["Year"])
print("Genre:", data["Genre"])
print("Plot:", data["Plot"])
print("Rating:", data["imdbRating"])
```

---

# 🌐 Code Example — Streamlit Version (movie_streamlit.py)

```python
import streamlit as st
import requests

st.title("🎬 Sabin's Movie Search App")

API_KEY = "YOUR_API_KEY"  # Insert your OMDb API key here

title = st.text_input("Enter movie title:", "Inception")

if st.button("Search"):
    url = f"https://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url)

    # Check API response status
    if response.status_code != 200:
        st.error("Error fetching data.")
    else:
        data = response.json()

        # When movie is not found
        if data["Response"] == "False":
            st.warning("Movie not found.")
        else:
            st.subheader(f"{data['Title']} ({data['Year']})")

            # Display poster image
            if data["Poster"] != "N/A":
                st.image(data["Poster"], width=300)
            else:
                st.info("No poster available.")

            # Show detailed info
            st.write(f"**Genre:** {data['Genre']}")
            st.write(f"**Rating:** ⭐ {data['imdbRating']}")
            st.write(f"**Plot:** {data['Plot']}")
```

---

# 📝 How to Run 

## ✔ 1) CLI Version

```bash
python3 movie.py
```

## ✔ 2) Streamlit Version

```bash
pip install streamlit
streamlit run movie_streamlit.py
```

---

# 📌 How to Get OMDb API Key

👉 [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)

* Select free key
* After type your e-mail and then get the key.

---

# 🔧 Future Improvements 

* Support multiple search results

* Show director & actors

* Add favorites system

* Caching API responses

* Save movie info in SQLite

* Improve Streamlit card-style UI

---

# 📜 License

MIT License


