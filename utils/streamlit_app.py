import streamlit as st
from recommender import recommend

st.title("🎬Recommendation movies")

st.markdown("Enter the movie title in English to get recommendations:")

movie_input = st.text_input("Movie title")

if st.button("Recommend"):
    if movie_input.strip() == "":
        st.warning("⚠️Enter the movie title.")
    else:
        result = recommend(movie_input)

        if isinstance(result, list):
            st.success("🎯 Recommended movies:")
            for i, movie in enumerate(result, 1):
                st.write(f"{i}. {movie}")
        else:
            st.error(result)
