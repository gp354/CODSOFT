import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Vectorize movie descriptions
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies['description'])

# Calculate cosine similarity
similarity = cosine_similarity(tfidf_matrix)

# Recommend function
def recommend(movie_title):
    if movie_title not in movies['title'].values:
        return ["❌ Movie not found in the database."]
    
    idx = movies[movies['title'] == movie_title].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    for i in sim_scores[1:4]:  # Top 3 similar movies
        recommended_movies.append(movies.iloc[i[0]]['title'])
    
    return recommended_movies

# Main Execution
if __name__ == "__main__":
    print("🎬 Movie Recommendation System 🎬")
    movie_input = input("Enter a movie title: ")
    print("\nTop Recommendations:")
    for rec in recommend(movie_input):
        print("👉", rec)
