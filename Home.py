import streamlit as st
import pandas as pd
import pymysql
from PIL import Image

st.sidebar.image(r"C:\Users\gowth\Downloads\Logo.jpeg")

# Home Page (Landing Page Content)
# Load your background image
bg_image = Image.open(r"C:\Users\gowth\Downloads\BgImage.jpeg") 

# Create two columns
col1, col2 = st.columns([1, 2])  # The number values control the width ratio (1:2 in this case)

# Display image in the first column
with col1:
    st.image(bg_image, width=2000)

# Display text in the second column
with col2:
    st.title("Tennis Sport Radar")
    st.write("\n")
    st.write("Game, Set, Data: Winning Insights at Your Fingertips.")
    
# Title of the page
st.title("Welcome to Tennis Sport Radar!")
st.write("\n")

