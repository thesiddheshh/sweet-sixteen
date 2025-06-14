import streamlit as st
from datetime import datetime
import pytz
import time
import json
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
from urllib.parse import urlparse, parse_qs
import base64

# ------------------------------
# Set page config
# ------------------------------
st.set_page_config(page_title="🎉 Sweet 16 Countdown", layout="wide")

# ------------------------------
# Load Lottie animation
# ------------------------------
def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

confetti_animation = load_lottie_file("assets/confetti.json")

# ------------------------------
# Timezone and birthday
# ------------------------------
IST = pytz.timezone("Asia/Kolkata")
birthday = IST.localize(datetime(2026, 3, 29, 0, 0, 0))

# ------------------------------
# Developer mode with query param
# ------------------------------
query_params = st.experimental_get_query_params()
dev = query_params.get("dev", [None])[0]

if dev == "siddhesh_supersecret":
    now = IST.localize(datetime(2026, 3, 29, 0, 0, 1))  # simulate bday
else:
    now = datetime.now(IST)

# ------------------------------
# CSS Styling and Background
# ------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

body {
    background-image: url("https://i.gifer.com/7efs.gif");
    background-size: cover;
    font-family: 'Quicksand', sans-serif;
    color: #333333;
}
.countdown {
    font-size: 2.5rem;
    text-align: center;
    margin-top: 20px;
    font-weight: bold;
}
.message {
    font-size: 1.2rem;
    text-align: center;
    color: #6a1b9a;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Header
# ------------------------------
st.image("stickers/balloon.png", width=80)
st.title("✨ Counting Down to a Magical Moment… ✨")
st.image("stickers/star.png", width=80)

if now < birthday:
    time_left = birthday - now
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    countdown_placeholder = st.empty()
    message_placeholder = st.empty()

    while datetime.now(IST) < birthday:
        now = datetime.now(IST)
        time_left = birthday - now
        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        countdown_html = f"""
        <div class="countdown">
            {days} Days | {hours} Hours | {minutes} Minutes | {seconds} Seconds
        </div>
        """
        countdown_placeholder.markdown(countdown_html, unsafe_allow_html=True)

        if days > 30:
            msg = "So many days left until your big day!"
        elif days > 10:
            msg = f"Only {days} days left until you turn 16!"
        elif days >= 1:
            msg = f"Just {days} days to go! You're almost there 👑"
        else:
            hrs = time_left.seconds // 3600
            msg = f"Less than {hrs} hours to go! The party's about to start 💖"

        message_placeholder.markdown(f"<p class='message'>{msg}</p>", unsafe_allow_html=True)
        time.sleep(1)
else:
    st_lottie(confetti_animation, speed=1, height=200, key="confetti")
    st.markdown("<h1 style='text-align:center;'>🎉 HAPPY 16TH BIRTHDAY!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:1.5rem;'>You're a star, never forget that ✨</p>", unsafe_allow_html=True)

    audio_file = open('assets/birthday_song.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3', autoplay=True)

    if st.button("🎁 Click to Open Your Gift"):
        st.balloons()
        st.success("Your gift has been opened!")

        st.subheader("💌 A Letter Just For You")
        with open("assets/letter.txt", "r") as f:
            st.write(f.read())

        st.subheader("📸 Our Memories")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("memories/mem1.jpg", use_column_width=True)
        with col2:
            st.image("memories/mem2.jpg", use_column_width=True)
        with col3:
            st.image("memories/mem3.jpg", use_column_width=True)

        st.subheader("🍰 Virtual Birthday Cake!")
        st.image("assets/cake.gif", use_column_width=True)

        st.subheader("🎧 Sweet 16 Vibes Playlist")
        st.write("Relax and celebrate with your favorite tunes:")
        st.markdown("""
        <iframe width="100%" height="300" src="https://www.youtube.com/embed/videoseries?list=YOUR_PLAYLIST_ID" frameborder="0" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

        st.subheader("🎀 16 Things I Love About You")
        love_list = [
            "You laugh at your own jokes and I love that.",
            "You make everything feel lighter.",
            "You're always up for an adventure.",
            "You dance like nobody’s watching.",
            "You know how to cheer me up.",
            "You're the kindest chaos I know.",
            "You're always honest, even when it’s hard.",
            "You have the best taste in music.",
            "You care deeply about people.",
            "You're brave in ways no one sees.",
            "You're loyal beyond words.",
            "You dream big and inspire others.",
            "You're creative and full of ideas.",
            "You're growing into someone amazing.",
            "You're unapologetically YOU.",
            "You're turning 16 and already shining bright ✨"
        ]
        for i, item in enumerate(love_list):
            st.markdown(f"{i+1}. {item}")

        mood = st.radio("How are you feeling today?", ("💭 Feeling nostalgic", "🥳 Feeling excited"))
        if mood == "💭 Feeling nostalgic":
            st.markdown("Let’s take a trip down memory lane...")
        else:
            st.markdown("Time to party! 🎉")

        if st.button("🍪 Tap to Open Fortune Cookie"):
            st.info("You are destined for greatness.")

st.markdown("---")
st.markdown("*Made with ❤️ for your Sweet 16 | Powered by Streamlit*")
