try it out -> https://movie-recommendation-system-fpurbffovkhsmn4hozsg6c.streamlit.app/

# 🎬 Movie Recommendation System

An AI-powered movie recommendation system built using the TMDb 5000 Movie Dataset. The project started as a simple content-based recommender using TF-IDF and cosine similarity, then evolved into a more intelligent recommendation system using semantic embeddings, fuzzy search, and a web interface.

---

## 📌 Problem

Initially, the system required users to enter the **exact movie title** stored in the dataset.

Example:

```text
Movie 'cars' not found in the dataset.

Enter a movie title: ocean

Movie 'ocean' not found in the dataset.

Enter a movie title: Pirates of the Caribbean

Movie 'Pirates of the Caribbean' not found in the dataset.

Enter a movie title: Pirates of the Caribbean: On Stranger Tides

Top 5 movies similar to 'Pirates of the Caribbean: On Stranger Tides':

1. Pirates of the Caribbean: The Curse of the Black Pearl
2. Pirates of the Caribbean: Dead Man's Chest
3. Pan
4. Highway
5. Ghost Rider
```

This approach was not user-friendly because users had to know and type the exact movie title stored in the dataset.

---

# 🚀 Improvements Made

## 1. Partial Search

The first improvement was adding **Partial Search**.

Partial search allows users to enter only part of a movie title and still find relevant results.

Example:

```text
cars
```

can match:

```text
Cars
Cars 2
Riding in Cars with Boys
```

### Benefits

* Easier movie discovery
* Better user experience
* No need to remember exact movie names

### Limitations

* Broad queries may return too many results
* Lower precision compared to exact matching
* Larger search indexes may affect performance

### Best Use Cases

* Autocomplete
* Flexible search
* Broad exploration

---

## 2. RapidFuzz Search

To improve search quality even further, I integrated **RapidFuzz**.

RapidFuzz performs fuzzy string matching using similarity algorithms such as Levenshtein Distance.

This allows the system to understand misspellings and typing mistakes.

Examples:

```text
intersteller
→ Interstellar

nemo
→ Finding Nemo

pirats
→ Pirates of the Caribbean
```

### Benefits

* Typo tolerance
* Improved user experience
* More natural search behavior

---

## 3. Replacing TF-IDF with Sentence Transformers

The original recommendation engine used:

* TF-IDF
* Cosine Similarity

While effective, TF-IDF focuses mainly on matching words rather than understanding meaning.

I upgraded the system to use **Sentence Transformers**.

### What are Sentence Transformers?

Sentence Transformers convert text into embeddings (numerical vectors) that capture semantic meaning.

Instead of matching exact words, the model understands the context and meaning of movie descriptions.

Example:

Movies with similar themes can be matched even if they do not share many common words.

### Benefits

* Semantic understanding
* Better recommendations
* Improved recommendation quality
* More human-like similarity matching

Model used:

```text
all-MiniLM-L6-v2
```

---

## 4. Embedding Caching

Generating embeddings for thousands of movies can take time.

To improve performance, I implemented **Embedding Caching**.

### What is Embedding Caching?

Embedding caching means saving generated embeddings to disk so they can be reused later.

Instead of regenerating embeddings every time the application starts:

```text
Generate embeddings
→ Save embeddings
→ Load embeddings on future runs
```

### Benefits

* Faster startup time
* Reduced computation
* Better user experience

---

## 5. Streamlit Web Interface

After improving the recommendation engine, I created a web interface using Streamlit.

The web application allows users to:

* Search for movies
* View movie information
* View recommendations
* See similarity scores

### Features

* Modern web interface
* Interactive search
* Recommendation display
* Movie details

---

## 6. Movie Posters with TMDB API

To improve the visual experience, I integrated the TMDB API.

The application now displays:

* Selected movie poster
* Recommended movie posters

This makes the application more visually appealing and easier to use.

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Sentence Transformers
* RapidFuzz
* Streamlit
* Requests
* TMDB API

---

# 📊 Dataset

This project uses the **TMDb 5000 Movie Dataset** from Kaggle.

Download the dataset here:

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Required files:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

---

# 🎯 Features

✅ Semantic Movie Recommendations

✅ Partial Search

✅ Fuzzy Search (RapidFuzz)

✅ Sentence Transformer Embeddings

✅ Similarity Score Display

✅ Embedding Caching

✅ Movie Posters

✅ Streamlit Web Interface

---

# Future Improvements

* Genre filtering
* Recommendation explanations
* User ratings
* Movie trailers
* Advanced search filters
* Deployment to the cloud

---

# Screenshots

Add screenshots of the Streamlit application here.

Example:

```text
assets/homepage.png
assets/recommendations.png
```

---

# Author

Omar Ibrahim

AI Engineer | Machine Learning | NLP | LLM Applications
