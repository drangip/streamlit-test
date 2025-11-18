#On importe les bibliothèques
import streamlit as st
import pandas as pd
import numpy as np

import kagglehub
# Download latest version
path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata")
print("Path to dataset files:", path)

#On ajoute un titre à l'application
st.title('Etude du TMDB 5000 Movie Dataset')

#Faire tourner streamlit
streamlit run streamtest.py
