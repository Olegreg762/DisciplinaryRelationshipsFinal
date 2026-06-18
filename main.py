import streamlit as st
import smtplib
from email.mime.text import MIMEText

def send_email():
    
    sender_email =st.secrets["SENDEMAIL"]
    sender_password = st.secrets["PASS"]
    body = "Application opened"

    msg = MIMEText(f"From: {sender_email}\n\n{body}")
    msg["Subject"] = body
    msg["From"] = sender_email
    msg["To"] = sender_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, sender_email, msg.as_string())
    except Exception as e:
        pass
    st.session_state.email_sent = True

if "email_sent" not in st.session_state:
    send_email()

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
    0: {"img": "resources/pdf/rationale.pdf"}, 
    1: {"img": "resources/image/slide0.png", "audio": "resources/audio/slide0.m4a", "notes": "resources/notes/slide0.txt"},
    2: {"img": "resources/image/slide1.png", "audio": "resources/audio/slide1.m4a", "notes": "resources/notes/slide1.txt"},
    3: {"img": "resources/image/slide2.png", "audio": "resources/audio/slide2.m4a", "notes": "resources/notes/slide2.txt"},
    4: {"img": "resources/image/slide3.png", "audio": "resources/audio/slide3.m4a", "notes": "resources/notes/slide3.txt"},
    5: {"img": "resources/image/slide4.png", "audio": "resources/audio/slide4.m4a", "notes": "resources/notes/slide4.txt"},
    6: {"img": "resources/image/slide5.png", "audio": "resources/audio/slide5.m4a", "notes": "resources/notes/slide5.txt"},
    7: {"img": "resources/image/slide6.png", "audio": "resources/audio/slide6.m4a", "notes": "resources/notes/slide6.txt"},
    8: {"img": "resources/image/slide7.png", "audio": "resources/audio/slide7.m4a", "notes": "resources/notes/slide7.txt"},
    9: {"img": "resources/image/slide8.png"},
    10: {"img": "resources/pdf/reflection.pdf"}
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
    
    st.image(slide_content[st.session_state.slide]["img"])

    if st.session_state.slide != len(slide_content) - 2:
        with open(slide_content[st.session_state.slide]["notes"], "r", encoding="utf-8") as file:
            file_contents = file.read()
        st.write(file_contents)

        st.audio(slide_content[st.session_state.slide]["audio"], autoplay=True)

elif st.session_state.slide == len(slide_content) - 1:
    st.header("End of Slideshow")
    st.subheader("Reflection")
    st.pdf(slide_content[st.session_state.slide]["img"], height=500)