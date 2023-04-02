import streamlit as st
import webbrowser

st.title(":red[Hello Everyone]!:wave:")
st.snow()

st.header("Streamlit Data App ")

st.subheader(":blue[G.Nikhil]")
st.caption("Data Science intern")

st.subheader("This is a Streamlit Data Web App:sunglasses:")
st.subheader("Create as a first assignment at innomatics research labs")


linkedin = 'https://linkedin.com/in/nikhil-gundlapelli'

if st.button('Linkedin'):
    webbrowser.open_new_tab(linkedin)


github = 'https://github.com/nikhilgundlapelli'

if st.button('Github'):
    webbrowser.open_new_tab(github)
 

btn_click = st.button("Hit me if its great!")

if btn_click == True:
    st.subheader("You clicked me :heart_eyes:")
    st.balloons()