import streamlit as st
import pickle
import requests

movies_list = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity_list.pkl", 'rb'))
movies_title_list = movies_list['title'].values

st.header("Movie Recommender System")
selected_value = st.selectbox("Select movie from dropdown", movies_title_list)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=6814924189ff9cf52097fec41a910b8b".format(movie_id)
    data = requests.get(url)
    data=data.json()
    path = data['poster_path']
    poster_path = "https://image.tmdb.org/t/p/w500"+ path
    return poster_path
    
def recommend(movies):
    index = movies_list[movies_list['title']==movies].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda vector:vector[1])
    recommend_movies=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id = movies_list.iloc[i[0]].id
        recommend_movies.append(movies_list.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))

    return recommend_movies, recommend_poster

if st.button("Show Reccommend"):
    movie_name, movie_poster = recommend(selected_value)
    col1,col2,col3,col4,col5 = st.columns(5)
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