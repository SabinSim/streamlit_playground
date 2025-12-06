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
