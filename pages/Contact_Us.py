import streamlit as st
from send_email import send_email

st.header('Contact Us')

with st.form(key='email_form'):
    user_email = st.text_input('Your email address')
    text_message = st.text_area('Your message')
    message = f"""\
Subject; New email from {user_email}
From: {user_email}
{text_message}

"""

    button = st.form_submit_button('Submit')
    if button:
        send_email(message, user_email)
        st.info("Your email has been sent successfuly")
        
