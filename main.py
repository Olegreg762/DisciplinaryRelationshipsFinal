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
    # 0 will be reserved for the rationale pdf and the final slide will be reserved for the reflection pdf
    0: {"img": "placeholder.pdf", "audio": "placeholder.mp3"},
    1: {"img": "placeholder.png", "audio": "placeholder.mp3", "notes": "placeholder.txt"},
}

col1, col2 = st.columns(2)
with col1:
    if st.session_state.slide == 0:
        pass
    else:
        st.button("Previous", on_click=prev_slide)

with col2:
    if st.session_state.slide == 0:
        st.button("Start Slideshow", on_click=next_slide)

    elif st.session_state.slide > 0 and st.session_state.slide < len(slide_content) - 1:
        st.button("Next", on_click=next_slide)
        
    elif st.session_state.slide == len(slide_content) - 1:
        st.button("Restart", on_click=next_slide)


if st.session_state.slide == 0:
    st.header("Rationale")
    st.pdf(slide_content[st.session_state.slide]["img"], height=500)

elif st.session_state.slide > 0 and st.session_state.slide < len(slide_content) - 1:
    
    st.image(slide_content[st.session_state.slide]["img"], caption=f"Slide {st.session_state.slide + 1}")

    with open(slide_content[st.session_state.slide]["notes"], "r", encoding="utf-8") as file:
        file_contents = file.read()
    st.write(file_contents)

    st.audio(slide_content[st.session_state.slide]["audio"], autoplay=True)

elif st.session_state.slide == len(slide_content) - 1:
    st.header("End of Slideshow")
    st.subheader("Reflection")
    st.pdf(slide_content[st.session_state.slide]["img"], height=500)