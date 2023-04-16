# OMDB-API

This project uses the Open Movie Database (OMDB) API to allow users to search for movies by title, browse movies by genre, and retrieve detailed information about a specific movie by its IMDB ID.

The project consists of three functions:

    search_movies_by_title: takes a movie title as input, sends a request to the OMDB API, and displays a list of movies that match the title, along with their year and IMDB ID.
    browse_movies_by_genre: takes a movie genre as input, sends a request to the OMDB API, and displays a list of movies in that genre, along with their year and IMDB ID.
    get_movie_by_id: takes a movie's IMDB ID as input, sends a request to the OMDB API, and displays detailed information about the movie, including its title, year, genre, IMDB rating, and plot.

Each function sends a request to the OMDB API using the requests module and parses the JSON response using the json module. The response is then checked to see if it contains the expected data, and if so, the relevant information is displayed to the user. If no movies are found or if the movie information is not available, an appropriate error message is displayed.

Overall, this project provides a simple interface for users to search and browse movies using the OMDB API.
