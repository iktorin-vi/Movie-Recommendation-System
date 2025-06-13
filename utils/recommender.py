import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("../data/processed_movies.csv")
df['soup'] = df['tags']

#CountVectorizer
vectorizer = CountVectorizer(max_features=5000, stop_words='english')
soup_vectors = vectorizer.fit_transform(df['soup'])

#Cosine similarity
similarity = cosine_similarity(soup_vectors)


def recommend(movie_title):
    movie_title = movie_title.lower()
    if movie_title not in df['title'].str.lower().values:
        return f"The movie '{movie_title}' was not found in the database."

    index = df[df['title'].str.lower() == movie_title].index[0]

    distances = list(enumerate(similarity[index]))

    movies_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    recommended_titles = [df.iloc[i[0]].title for i in movies_list]
    return recommended_titles