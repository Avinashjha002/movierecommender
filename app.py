import streamlit as st
import pickle
import requests

movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender App")
select_value = st.selectbox("Select Movie from Dropdown", movies_list)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=423d13b5213aa46cc0a8fae35e7add52&language=en-us".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda vector:vector[1])
    recommend_movies = []
    recommend_poster = []
    for i in distance[1:21]:
        movies_id = movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movies, recommend_poster

if st.button("Recommend"):
    movie_name, movie_poster = recommend(select_value)
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    col11, col12, col13, col14, col15 = st.columns(5)
    col16, col17, col18, col19, col20 = st.columns(5) 
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
    with col6:
        st.text(movie_name[5])
        st.image(movie_poster[5])
    with col7:
        st.text(movie_name[6])
        st.image(movie_poster[6])
    with col8:
        st.text(movie_name[7])
        st.image(movie_poster[7])
    with col9:
        st.text(movie_name[8])
        st.image(movie_poster[8])
    with col10:
        st.text(movie_name[9])
        st.image(movie_poster[9])
    with col11:
        st.text(movie_name[10])
        st.image(movie_poster[10])
    with col12:
        st.text(movie_name[11])
        st.image(movie_poster[11])
    with col13:
        st.text(movie_name[12])
        st.image(movie_poster[12])
    with col14:
        st.text(movie_name[13])
        st.image(movie_poster[13])
    with col15:
        st.text(movie_name[14])
        st.image(movie_poster[14])
    with col16:
        st.text(movie_name[15])
        st.image(movie_poster[15])
    with col17:
        st.text(movie_name[16])
        st.image(movie_poster[16])
    with col18:
        st.text(movie_name[17])
        st.image(movie_poster[17])
    with col19:
        st.text(movie_name[18])
        st.image(movie_poster[18])
    with col20:
        st.text(movie_name[19])
        st.image(movie_poster[19])