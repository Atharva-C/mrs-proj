import streamlit as st
import pickle
import pandas as pd


# Load your custom CSS from the file
with open("styles.css") as f:
    custom_css = f.read()

# Apply the custom CSS using st.markdown()
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
similarity = pd.DataFrame(similarity)


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which movie u want to watch today?',
    movies['title'].values)

if st.button('recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

