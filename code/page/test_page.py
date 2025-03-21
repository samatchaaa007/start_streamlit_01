import streamlit as st
import pandas as pd

# Page Title
st.title("Getting Started with Streamlit")
st.write("This is an introduction to Streamlit")

# Displaying Source Code
st.markdown("## Source Code")
with st.echo():
    st.markdown("### Code Example")
    
    code = '''
def hello():
    print("Hello, Streamlit!")
    '''
    
    # Button to Show Code
    show_btn = st.button("Show code!")
    if show_btn:
        st.code(code, language='python')

# Creating Two Columns
cols = st.columns(2)

with cols[0]:
    age_inp = st.number_input("Input your age")
    st.markdown(f"Your age is {round(age_inp, 2)}")

with cols[1]:
    text_inp = st.text_input("Input your text")
    word_tokenize = "|".join(text_inp.split())
    st.markdown(f"Tokenized text: {word_tokenize}")

# Creating a DataFrame
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 60, 90]
})
st.dataframe(df)

# Button to Show Chart
if st.button("Show Chart!!"):
    st.line_chart(df, x='first column', y='second column')
