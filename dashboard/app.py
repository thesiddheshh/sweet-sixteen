# sweet16_birthday_app/app.py
import streamlit as st
import time
from datetime import datetime
import pytz
import json
from streamlit_lottie import st_lottie
import random
import os

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(page_title="Sweet 16 Countdown", layout="centered")

# Set timezone and birthday
IST = pytz.timezone("Asia/Kolkata")
birthday = IST.localize(datetime(2026, 3, 29, 0, 0, 0))

# ----------------------------
# STYLING
# ----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&display=swap');
html, body, [class*="css"]  {
    font-family: 'Quicksand', sans-serif;
    background: url('https://i.pinimg.com/originals/13/f3/5a/13f35a8aeff67c8022fa6f3853db507c.gif') no-repeat center center fixed;
    background-size: cover;
    color: #4b004b;
}
h1, h2, h3, h4 {
    color: #8e44ad;
}
.countdown {
    font-size: 2.8rem;
    font-weight: bold;
    color: #ff69b4;
    text-align: center;
    margin-bottom: 10px;
}
.message {
    font-size: 1.2rem;
    text-align: center;
    color: #6a1b9a;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# LOAD LOTTIE
# ----------------------------
def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

confetti = load_lottie_file("assets/confetti.json")

# ----------------------------
# HEADER
# ----------------------------
st.markdown("""
<h1 style='text-align: center;'>🎀 Sweet 16 Countdown 🎀</h1>
<p class='message'>Counting every moment until the p-day...</p>
""", unsafe_allow_html=True)

# ----------------------------
# LIVE COUNTDOWN
# ----------------------------
if datetime.now(IST) < birthday:
    countdown_placeholder = st.empty()
    message_placeholder = st.empty()

    while datetime.now(IST) < birthday:
        now = datetime.now(IST)
        time_left = birthday - now
        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        countdown_html = f"""
            <div class='countdown'>
                {days} Days : {hours} Hours : {minutes} Minutes : {seconds} Seconds
            </div>
        """
        countdown_placeholder.markdown(countdown_html, unsafe_allow_html=True)

        # Message logic
        if days > 30:
            msg = "Still so many days tsk"
        elif days > 10:
            msg = f"Only {days} days to go until you're 16! 💖"
        elif days >= 1:
            msg = f"Just {days} days to go! It's almost here 👑"
        else:
            msg = f"Less than a day left! Get ready to sparkle ✨"

        message_placeholder.markdown(f"<p class='message'>{msg}</p>", unsafe_allow_html=True)
        time.sleep(1)

else:
    # ----------------------------
    # BIRTHDAY UNLOCKED
    # ----------------------------
    st_lottie(confetti, speed=1, height=300)
    st.markdown("""
    <h1 style='text-align:center;'>🎉 HAPPY SWEET 16!</h1>
    <p style='text-align:center; font-size:1.5rem;'>Today is your day, and you're loved more than ever 💕</p>
    """, unsafe_allow_html=True)

    st.audio("assets/birthday_song.mp3", format="audio/mp3", autoplay=True)

    # 🎁 Click to open surprise
    if st.button("🎁 Click to Open Your Gift"):
        st.balloons()
        st.success("Your surprises are here!")

        # 💌 Future Letter
        st.subheader("💌 A Letter From Your Future Self")
        with open("assets/letter.txt", "r") as f:
            st.write(f.read())

        # 📸 Scrapbook
        st.subheader("📸 Our Memories")
        images = [f"memories/{img}" for img in os.listdir("memories") if img.endswith(".jpg") or img.endswith(".png")]
        st.image(images, width=300, caption=["Memory" for _ in images])

        # 🍰 Cake GIF
        st.subheader("🍰 Blow the Candle")
        if st.button("🕯️ Blow Candle"):
            st.image("assets/cake.gif", use_column_width=True)

        # 🎧 Playlist
        st.subheader("🎧 Sweet 16 Playlist")
        st.markdown("""
        <iframe style='border-radius:12px' src='https://open.spotify.com/embed/playlist/YOUR_PLAYLIST_ID' width='100%' height='380' frameBorder='0' allowfullscreen='' allow='autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture'></iframe>
        """, unsafe_allow_html=True)

        # 🎀 16 Things I Love
        st.subheader("🎀 16 Things I Love About You")
        with st.container():
            reasons = [
                "You laugh at your own jokes!",
                "You make everything feel better.",
                "You light up every room.",
                "You care deeply.",
                "You're brave beyond measure.",
                "You're full of life and dreams.",
                "You have the best hugs.",
                "You're thoughtful and kind.",
                "You're effortlessly funny.",
                "You're my favorite chaos.",
                "You're honest and real.",
                "You're the kind of friend I wished for.",
                "You're magic wrapped in stardust.",
                "You're beautiful inside out.",
                "You're stronger than you think.",
                "You're turning 16 and glowing brighter than ever!"
            ]
            for i, reason in enumerate(reasons):
                st.markdown(f"**{i+1}.** {reason}")

        # 🍪 Fortune Cookie
        st.subheader("🍪 Open Your Fortune Cookie")
        if st.button("Crack Cookie"):
            fortunes = [
                "You're destined for greatness!",
                "Magic follows you everywhere.",
                "You are more loved than you realize.",
                "Something amazing is on the way.",
                "You sparkle even when it's dark."
            ]
            st.info(random.choice(fortunes))

        # 🧠 Quiz
        st.subheader("🧠 Sweet 16 Quiz")
        q1 = st.radio("What’s your comfort food?", ["Pizza", "Ice cream", "Noodles"])
        q2 = st.radio("Your favorite memory together?", ["Laughing till we cried", "Secret sharing", "Late night talks"])
        if st.button("Submit Quiz"):
            st.success("You're 100% unique and 1000% amazing 💜")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Made with ❤️ by your seventh favourite friend</p>", unsafe_allow_html=True)
