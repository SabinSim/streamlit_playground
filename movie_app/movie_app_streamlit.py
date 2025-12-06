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
