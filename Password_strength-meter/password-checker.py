# import streamlit as st
# import re

# st.set_page-config(page_title="Password Strength Checker") # type: ignore


# st.title ("Pasword Strength Checker")
# st.markdown("""  "##Welcome to the ultimate password strength checker":  use this simple tool to check strength of your password and et suggestion on how to make it strange.
#             we will give you helpful tips to create a  **Strength Password**   """)

# password = st.test_input("Enter your password", type="password")
 
# feedback = []

# score = 0

# if password:
#     if len(password) >= 8:
#         score += 1
#     else :
#             feedback.append("Password should be at least  8 chaeacteristics long.")

# if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
#      score +=1

# else: 
#      feedback.append()


import streamlit as st
import re

# Set page title
st.set_page_config(page_title="Password Strength Checker")

# Page heading
st.title("Password Strength Checker")

# Intro text
st.markdown("""
## Welcome to the Ultimate Password Strength Checker  
Use this simple tool to check how strong your password is and get tips to improve it.  
We’ll help you create a **strong and secure password**!
""")

# Input field for password
password = st.text_input("Enter your password", type="password")

# Variables to track score and suggestions
feedback = []
score = 0

# Check password strength
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔸 Use both uppercase and lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔸 Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("🔸 Include at least one special character (!@#$ etc.).")

    # Display score
    st.markdown(f"**Password Strength Score:** {score} / 4")

    # Show suggestions
    if feedback:
        st.markdown("### Suggestions to Improve Your Password:")
        for tip in feedback:
            st.write(tip)
    else:
        st.success("✅ Great job! Your password is strong.")




