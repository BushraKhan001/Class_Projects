import streamlit as st
import re

st.set_page-config(page_title="Password Strength Checker") # type: ignore


st.title ("Pasword Strength Checker")
st.markdown("""  "##Welcome to the ultimate password strength checker":  use this simple tool to check strength of your password and et suggestion on how to make it strange.
            we will give you helpful tips to create a  **Strength Password**   """)

password = st.test_input("Enter your password", type="password")
 
feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else :
            feedback.append("Password should be at least  8 chaeacteristics long.")

if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
     score +=1

else: 
     feedback.append()






