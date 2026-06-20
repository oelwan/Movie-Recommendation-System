from rapidfuzz import process, fuzz
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import ast
import os
import pickle
import requests
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

"""
# -----------------------------
# 3. Vectorization
# -----------------------------
vectorizer = TfidfVectorizer(stop_words='english')
feature_matrix = vectorizer.fit_transform(df['combined_features'])

# -----------------------------
# 4. Similarity Calculation
# -----------------------------
similarity = cosine_similarity(feature_matrix)
"""
""
"""
# -----------------------------
# 3. Sentence Transformer Embeddings
# -----------------------------

print("Loading embedding model...")

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

print("Generating movie embeddings...")

embeddings = model.encode(
    df['combined_features'].tolist(),
    show_progress_bar=True
)

# -----------------------------
# 4. Similarity Calculation
# -----------------------------

similarity = cosine_similarity(embeddings)

"""

EMBEDDINGS_FILE = "movie_embeddings.pkl"

if os.path.exists(EMBEDDINGS_FILE):

    print("Loading saved embeddings...")

    with open(EMBEDDINGS_FILE, "rb") as f:
        embeddings = pickle.load(f)

else:

    print("Loading embedding model...")

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    print("Generating movie embeddings...")

    embeddings = model.encode(
        df['combined_features'].tolist(),
        show_progress_bar=True
    )

    with open(EMBEDDINGS_FILE, "wb") as f:
        pickle.dump(embeddings, f)

    print("Embeddings saved!")

similarity = cosine_similarity(embeddings)

#--------------------------
#this is for partial search 
"""
def find_matching_movies(query, df=df):
    matches = df[
        df['title'].str.contains(query, case=False, na=False)
    ]['title'].tolist()

    return matches
"""

#------------------------
#Add a Fuzzy Search Function

def find_best_match(query, df=df):

    titles = df['title'].tolist()

    match = process.extractOne(
        query,
        titles,
        scorer=fuzz.WRatio,
        score_cutoff=70
    )

    if match:
        return match[0]

    return None

#---------------------


# -----------------------------
# 5. Recommendation Function
# -----------------------------
def recommend_movies(title, df=df, similarity=similarity, top_n=5):

    # Exact match not found
    if title not in df['title'].values:

        # Try partial search first
        matches = df[
            df['title'].str.contains(title, case=False, na=False)
        ]['title'].tolist()

        if len(matches) > 0:

            # Automatically use first match
            title = matches[0]

        else:

            # Fall back to RapidFuzz
            best_match = find_best_match(title)

            if best_match:

                title = best_match

            else:

                return None

    # Get movie index
    idx = df[df['title'] == title].index[0]

    # Calculate similarity scores
    sim_scores = list(enumerate(similarity[idx]))

    sim_scores = sorted(
        sim_scores,
        key=lambda x: x[1],
        reverse=True
    )

    sim_scores = sim_scores[1:top_n + 1]

    recommendations = []

    for movie_index, score in sim_scores:

        movie_title = df['title'].iloc[movie_index]

        recommendations.append(
            (movie_title, score)
        )

    return title, recommendations

#------------------------------------------

TMDB_API_KEY = "1e8eb1261af27a148144637b1c1415d7"

def get_movie_poster(movie_title):

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": movie_title
    }

    response = requests.get(url, params=params)

    data = response.json()

    if data["results"]:

        poster_path = data["results"][0]["poster_path"]

        if poster_path:

            return (
                "https://image.tmdb.org/t/p/w500"
                + poster_path
            )

    return None


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
        result = recommend_movies(user_input)

        if result:

            selected_title, recommendations = result

            # Get movie information
            selected_movie = df[df['title'] == selected_title].iloc[0]

            print("\n" + "="*50)
            print(f"Selected Movie: {selected_title}")

            print(f"Genres: {selected_movie['genres_clean']}")
            print(f"Director: {selected_movie['director_clean']}")
            print("="*50)

            print(f"\nTop 5 movies similar to '{selected_title}':")

            for i, (movie, score) in enumerate(recommendations, 1):

                percentage = round(score * 100)

                print(f"{i}. {movie} ({percentage}%)")

            print()

if __name__ == "__main__":
    main() 