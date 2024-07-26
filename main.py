import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

#
# with open('wave.css') as f:
#     css = f.read()

#st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

with col1:
    st.image("images/photo.png", width=500)

with col2:
    st.title("Aashritha L S")
    content = """
    Hi, I am Aashritha! I am a Software Developer 
    and Data scientist. I am currently doing my 
    masters at Uni Kassel.  
    """
    st.info(content)

content2 = """
Below you can find some of the apps
I have built in Python. 
Feel free to contact me! :)
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"],width = 300)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"], width = 300)
        st.write(f"[Source Code]({row['url']})")





