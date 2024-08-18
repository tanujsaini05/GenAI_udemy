import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello ji!")
st.text('''This is our First Streamlit App\nNow we will progress Consistently in life either it is coding or daily life.''')
st.button("love You")

data=pd.DataFrame(
    {'FirstCol' : [1,22,3,4,5,6,7,8,9],
    "SecondCol" : [10,11,12,13,14,15,16,17,18]}
)

st.write(data)

chart_data = pd.DataFrame(
        np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)