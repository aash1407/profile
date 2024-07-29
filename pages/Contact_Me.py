import streamlit as st
from send_email import send_email
st.header("Contact Me")

with st.form(key='email_form'):
    user_email = st.text_input("Your email address", key="user_email")
    subject = st.selectbox("Select the subject",("General questions","Connect request","Interview/job offer","Collaboration","Other"))
    message = st.text_area("Your message")
    message = message
    submit = st.form_submit_button("Submit")
    if submit:
        send_email(message, user_email, subject)
        st.info("Your email was sent successfully!")

