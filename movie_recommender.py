import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

# -----------------------------
# 1. Load the Dataset
# -----------------------------
MOVIES_PATH = 'tmdb_5000_movies.csv'
CREDITS_PATH = 'tmdb_5000_credits.csv'

# Load datasets
df_movies = pd.read_csv(MOVIES_PATH)
df_credits = pd.read_csv(CREDITS_PATH)

# -----------------------------
# 2. Data Cleaning & Merging
# -----------------------------
# Merge credits into movies on 'id'
df_credits = df_credits.rename(columns={'movie_id': 'id'})
df = df_movies.merge(df_credits, on='id')

# Ensure the correct title column is used after merge
if 'title_x' in df.columns:
    df = df.rename(columns={'title_x': 'title'})
elif 'title' not in df.columns and 'title_y' in df.columns:
    df = df.rename(columns={'title_y': 'title'})

# Fill missing overviews with empty string
df['overview'] = df['overview'].fillna('')

# Helper functions to parse features
def parse_genres(genres_str):
    try:
        genres = ast.literal_eval(genres_str)
        return ' '.join([g['name'] for g in genres])
    except:
        return ''

def get_top_cast(cast_str, top_n=3):
    try:
        cast = ast.literal_eval(cast_str)
        return ' '.join([c['name'] for c in cast[:top_n]])
    except:
        return ''

def get_director(crew_str):
    try:
        crew = ast.literal_eval(crew_str)
        for c in crew:
            if c['job'] == 'Director':
                return c['name']
        return ''
    except:
        return ''

# Apply feature extraction
df['genres_clean'] = df['genres'].apply(parse_genres)
df['cast_clean'] = df['cast'].apply(get_top_cast)
df['director_clean'] = df['crew'].apply(get_director)

# Combine features into a single string
def combine_features(row):
    return (
        row['genres_clean'] + ' ' +
        row['overview'] + ' ' +
        row['cast_clean'] + ' ' +
        row['director_clean']
    )

df['combined_features'] = df.apply(combine_features, axis=1)

# -----------------------------
# 3. Vectorization
# -----------------------------
vectorizer = TfidfVectorizer(stop_words='english')
feature_matrix = vectorizer.fit_transform(df['combined_features'])

# -----------------------------
# 4. Similarity Calculation
# -----------------------------
similarity = cosine_similarity(feature_matrix)

# -----------------------------
# 5. Recommendation Function
# -----------------------------
def recommend_movies(title, df=df, similarity=similarity, top_n=5):
    """
    Given a movie title, return the top N most similar movies.
    """
    if title not in df['title'].values:
        print(f"Movie '{title}' not found in the dataset.")
        return []
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]  # Exclude the movie itself
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

# -----------------------------
# 6. User Interaction
# -----------------------------
def main():
    print("\n=== Movie Recommendation System ===")
    print("Type a movie title (as in the dataset) to get recommendations.")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("Enter a movie title: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        recommendations = recommend_movies(user_input)
        if recommendations:
            print(f"\nTop 5 movies similar to '{user_input}':")
            for i, rec in enumerate(recommendations, 1):
                print(f"{i}. {rec}")
            print()

if __name__ == "__main__":
    main() 