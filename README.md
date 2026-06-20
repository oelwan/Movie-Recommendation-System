# 🎬 Movie Recommendation System (Content-Based Filtering)

A content-based Movie Recommendation System built with Python and Machine Learning techniques using the TMDb 5000 Movie Dataset from Kaggle.

The system recommends movies similar to a selected movie by analyzing genres, plot overviews, cast members, and directors using Natural Language Processing (NLP) techniques.

---

## 🚀 Features

### Current Features

* Cleans and preprocesses the dataset
* Combines multiple movie attributes:

  * Genres
  * Overview
  * Top Cast Members
  * Director
* TF-IDF Vectorization
* Cosine Similarity Matching
* Partial Movie Title Search
* RapidFuzz Fuzzy Matching
* Intelligent Suggestions When a Movie Is Not Found
* Similarity Score Display
* Top 5 Movie Recommendations
* Interactive Command-Line Interface (CLI)

---

## 🧠 How It Works

### 1. Data Preprocessing

The system extracts and cleans movie information from the dataset:

* Genres
* Overview
* Cast
* Director

These features are combined into a single text representation for each movie.

### 2. Feature Vectorization

Movie descriptions are transformed into numerical vectors using TF-IDF:

```python
TfidfVectorizer(stop_words="english")
```

### 3. Similarity Calculation

The similarity between movies is calculated using Cosine Similarity:

```python
cosine_similarity(feature_matrix)
```

### 4. Recommendation Generation

When a user enters a movie title:

1. The movie is located in the dataset.
2. Similarity scores are calculated.
3. Movies are ranked by similarity.
4. The top recommendations are displayed.

### 5. Smart Search

If an exact movie title is not found:

* Partial matching is performed.
* RapidFuzz searches for the closest titles.
* Matching suggestions are displayed automatically.

---

## 📊 Dataset

This project uses the **TMDb 5000 Movie Dataset** from Kaggle.

Download the dataset here:

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Required files:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* RapidFuzz
* TF-IDF
* Cosine Similarity
* NLP Techniques

---

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── movie_recommender.py
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Download the Dataset

Download the TMDb 5000 Movie Dataset from Kaggle and place the following files in the project directory:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

### 5. Run the Project

```bash
python movie_recommender.py
```

---

## 📌 Example Usage

```text
Enter a movie title: batman

Possible matches:

1. Batman Begins
2. Batman Returns
3. Batman Forever

Select a movie: 1

Top 5 movies similar to 'Batman Begins':

1. The Dark Knight (91.4%)
2. The Dark Knight Rises (89.2%)
3. Batman (84.8%)
4. Man of Steel (80.5%)
5. Watchmen (78.1%)
```

---

## 📈 Future Improvements

* Sentence Transformers Semantic Search
* Embedding-Based Recommendations
* Streamlit Web Application
* FastAPI Deployment
* Movie Posters Integration
* Personalized Recommendations
* Hybrid Recommendation System

---

## 🎯 Learning Outcomes

This project demonstrates:

* Recommendation Systems
* Natural Language Processing (NLP)
* Feature Engineering
* Information Retrieval
* Fuzzy String Matching
* Machine Learning Fundamentals
* Python Data Processing

---

## 👨‍💻 Author

**Omar ibrahim**

AI Engineer | Machine Learning Enthusiast


