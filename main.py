import streamlit as st

st.title("Disciplinary Relationships Final Project")

if "slide" not in st.session_state:
    st.session_state.slide = 0

def next_slide():
    st.session_state.slide += 1
    if st.session_state.slide > len(slide_content) - 1:
        st.session_state.slide = 0

def prev_slide():
    st.session_state.slide -= 1
    if st.session_state.slide < 0:
        st.session_state.slide = len(slide_content) - 1

slide_content ={

}

