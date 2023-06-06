class Movie:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title, genre):
        movie_id = len(self.movies) + 1
        self.movies[movie_id] = {"title": title, "genre": genre}

    def get_movie_id(self, title):
        for movie_id, movie_info in self.movies.items():
            if movie_info["title"] == title:
                return movie_id
        return None

    def get_movie_title(self, movie_id):
        return self.movies.get(movie_id)["title"]

    def get_all_movies(self):
        return self.movies
