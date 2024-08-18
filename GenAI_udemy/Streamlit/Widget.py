import streamlit as st
import pandas as pd
import numpy as np


st.title("Let's start working on Streamlit a little more")

name= st.text_input("Name ")

if name:
    st.write(f'Hello {name}')

age = st.slider("Select Your age  :: ",1,100,20)
st.write(f"Your age is {age}")

options=["Python","C++","Java",'C#']
st.selectbox("Choose your language ",options=options )
