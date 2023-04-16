import requests

# Define the OMDB API endpoint and your API key
OMDB_ENDPOINT = "http://www.omdbapi.com/"
OMDB_API_KEY = "<your_api_key_here>"

def search_movies_by_title(title):
    # Set up the API parameters
    params = {
        "apikey": OMDB_API_KEY,
        "s": title,
        "type": "movie"
    }

    # Send the API request
    response = requests.get(OMDB_ENDPOINT, params=params)

    # Parse the response JSON
    data = response.json()

    # Check if the request was successful
    if data["Response"] == "True":
        # Display the movie information
        for movie in data["Search"]:
            print("Title:", movie["Title"])
            print("Year:", movie["Year"])
            print("IMDB ID:", movie["imdbID"])
            print()
    else:
        print("No movies found with that title")

def browse_movies_by_genre(genre):
    # Set up the API parameters
    params = {
        "apikey": OMDB_API_KEY,
        "s": "",
        "type": "movie",
        "genre": genre
    }

    # Send the API request
    response = requests.get(OMDB_ENDPOINT, params=params)

    # Parse the response JSON
    data = response.json()

    # Check if the request was successful
    if data["Response"] == "True":
        # Display the movie information
        for movie in data["Search"]:
            print("Title:", movie["Title"])
            print("Year:", movie["Year"])
            print("IMDB ID:", movie["imdbID"])
            print()
    else:
        print("No movies found in that genre")

def get_movie_by_id(imdb_id):
    # Set up the API parameters
    params = {
        "apikey": OMDB_API_KEY,
        "i": imdb_id,
        "plot": "full"
    }

    # Send the API request
    response = requests.get(OMDB_ENDPOINT, params=params)

    # Parse the response JSON
    data = response.json()

    # Check if the request was successful
    if data["Response"] == "True":
        # Display the movie information
        print("Title:", data["Title"])
        print("Year:", data["Year"])
        print("Genre:", data["Genre"])
        print("IMDB Rating:", data["imdbRating"])
        print("Plot:", data["Plot"])
        print()
    else:
        print("Movie not found with that IMDB ID")

# Example usage
search_movies_by_title("The Dark Knight")
browse_movies_by_genre("Action")
get_movie_by_id("tt0468569")  # The Dark Knight IMDB ID
