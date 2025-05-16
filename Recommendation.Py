import pandas as pd

# Sample data: movies with genres
movies = pd.DataFrame({
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['Inception', 'Titanic', 'Toy Story', 'The Avengers', 'The Godfather'],
    'genres': [
        ['Action', 'Sci-Fi'],
        ['Romance', 'Drama'],
        ['Animation', 'Family'],
        ['Action', 'Adventure'],
        ['Crime', 'Drama']
    ]
})

def format_genres(genres):
    return " | ".join(genres)

def recommend_movies(movies, user_preferences, top_n=3):
    def score(genres):
        return len(set(genres) & set(user_preferences))
    movies['score'] = movies['genres'].apply(score)
    recommendations = movies[movies['score'] > 0].sort_values(by='score', ascending=False)
    return recommendations[['title', 'genres', 'score']].head(top_n)

def get_user_preferences():
    print("🎬 Welcome to the Movie Recommendation System! 🎬")
    print("Please enter your favorite genres, separated by commas (e.g. Action, Drama, Comedy):")
    user_input = input("Your favorite genres: ")
    preferences = [genre.strip().title() for genre in user_input.split(',') if genre.strip()]
    return preferences

# Get user preferences with input
user_preferences = get_user_preferences()

# Get recommendations
recommendations = recommend_movies(movies, user_preferences)

# Print results in a pretty way
print("\n✨✨✨  Movie Recommendations For You!  ✨✨✨\n")
for idx, row in recommendations.iterrows():
    print(f"🎬 {row['title']}")
    print(f"   Genres: {format_genres(row['genres'])}")
    print(f"   Match Score: {row['score']} 🌟\n")
print("Enjoy your movie time! 🍿")