# Movie Recommendation System (Content-Based Filtering)

This project is a content-based movie recommendation system using the TMDb 5000 Movie Dataset from Kaggle.

## Features
- Cleans and preprocesses the dataset
- Combines relevant features (genres, overview, cast, director)
- Uses TF-IDF vectorization and cosine similarity
- Returns top 5 similar movies for a given title

## Setup Instructions

### 1. Clone the Repository
Clone or download this project to your local machine.

### 2. Create and Activate a Virtual Environment
```
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Required Packages
```
pip install -r requirements.txt
```

### 4. Download the Dataset
Download the [TMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle.
Place the following files in the project directory:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

### 5. Run the Script
```
python movie_recommender.py
```

Or, to explore interactively:
```
jupyter notebook
```

## Usage
The script will prompt you to enter a movie title and will return the top 5 similar movies based on content features.

## Requirements
See `requirements.txt` for all dependencies.

## Notes
- Ensure the dataset CSV files are in the same directory as the script.
- For best results, use exact movie titles as found in the dataset. 