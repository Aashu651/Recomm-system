import streamlit as st
import pickle

import pandas as pd

import numpy as np





def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for j in movies_list:
        recommended_movies.append(movie_list.iloc[j[0]].title)
    return recommended_movies





movie_dct=pickle.load(open('movie_dct.pkl','rb'))
movie_list=pd.DataFrame(movie_dct)

similarity=pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list['title'].values)
if st.button('Show Recommendation'):
    recommendations = recommend(selected_movie)

    for i in recommendations:
        st.write(i)
