import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width = 400)

with col2:
    st.title("Aashritha L S")
    content = """
    Hi, I am Aashritha! I am a Software Developer 
    and Data scientist. I am currently doing my 
    masters at Uni Kassel.  
    """
    st.info(content)


