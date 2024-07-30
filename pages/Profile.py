import streamlit as st
import pandas
import requests
from streamlit_lottie import st_lottie

st.set_page_config(layout="wide")

# col1, col2 = st.columns([1.5, 3.5])

st.image("images/Data Scientist.png", width=500)
def lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#
#
# lottie_1 = lottie_url("https://lottie.host/e808ddb0-7857-44ed-ac98-6d0c5c02625c/T93xtmv2Tn.json")
#
# with open('wave.css') as f:
#     css = f.read()

# st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
#
# with col1:
#     st.image("images/photo.png", width=300)
#
# with col2:
#     st.title("Aashritha L S")
#     content = """
#     Hey there! :wave:'\n
#     I am Aashritha!\n
#     I am a Software Developer,
#     Data scientist and AI enthusiast.
#     I have worked as a software developer at Cognizant.
#     I am currently doing my
#     masters at Uni Kassel.
#     I am also working as a data scientist part-time at the Uni Kassel
#     where I focus on developing solutions for Car-to-Pedestrian collision
#     avoidance mainly using Artificial Neural Networks.
#     """
#
#     mystyle = '''
#         <style>
#             p {
#                 text-align: justify;
#             }
#         </style>
#         '''
#
#     st.markdown(mystyle, unsafe_allow_html=True)
#     st.info(content)

content2 = """
Below you can find some of the apps
I have built in Python. 
Feel free to contact me! :)\n
\n
\n

"""
st.write("---")
st.markdown(f'<span style="font-size: 24px;">{content2}</span>', unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.0, 0.5, 1.0])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
#        st_lottie(lottie_1, width=400)
        # st.image("images/" + row["image"])
        st_lottie(lottie_url(row["image"]), width=400)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        #st.image("images/" + row["image"])
        st_lottie(lottie_url(row["image"]), width=400)
        st.write(f"[Source Code]({row['url']})")
