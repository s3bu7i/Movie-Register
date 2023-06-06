from user import User
from movie import Movie
from recommendation import Recommendation

# Create instances of User, Movie, and Recommendation classes
user = User()
movie = Movie()
recommendation = Recommendation()

# User registration and login
user.register()
user.login()

# Movie data initialization
movie.add_movie("Movie 1", "Action")
movie.add_movie("Movie 2", "Drama")
movie.add_movie("Movie 3", "Comedy")

# User rates movies
user.rate_movie(movie.get_movie_id("Movie 1"), 4)
user.rate_movie(movie.get_movie_id("Movie 2"), 5)
user.rate_movie(movie.get_movie_id("Movie 3"), 3)

# Get movie recommendations for the user
recommended_movies = recommendation.get_recommendations(user.get_user_id(), movie.get_all_movies())

# Display recommended movies
print("Recommended Movies:")
for movie_id, score in recommended_movies:
    print(movie.get_movie_title(movie_id), "(Score:", score, ")")
