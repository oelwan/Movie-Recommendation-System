import streamlit as st
from movie_recommender import (
    recommend_movies,
    df,
    get_movie_poster
)
from movie_recommender import recommend_movies, df

import streamlit as st
from movie_recommender import recommend_movies, df

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬"
)

st.title("🎬 Movie Recommendation System")

movie_name = st.text_input(
    "Enter a movie title"
)

if st.button("Recommend"):

    if movie_name:

        result = recommend_movies(movie_name)

        if result:

            selected_title, recommendations = result

            selected_movie = df[
                df['title'] == selected_title
            ].iloc[0]

            st.subheader(selected_title)
            poster = get_movie_poster(selected_title)

            if poster:
                st.image(
                    poster,
                    width=250
                )
            st.write(
                f"**Genres:** {selected_movie['genres_clean']}"
            )

            st.write(
                f"**Director:** {selected_movie['director_clean']}"
            )
            
            st.write("### Overview")

            st.write(
                selected_movie['overview']
            )
            st.markdown("---")

            st.subheader("Recommendations")

            cols = st.columns(5)

            for i, (movie, score) in enumerate(recommendations):

                poster = get_movie_poster(movie)

                percentage = round(score * 100)

                with cols[i]:

                    if poster:
                        st.image(poster)

                    st.caption(movie)

                    st.progress(percentage / 100)

                    st.write(f"{percentage}%")