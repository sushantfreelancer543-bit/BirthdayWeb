import streamlit as st

# Page setup
st.set_page_config(page_title="Happy Birthday ❤️", layout="centered")

# Background CSS with your GitHub raw image link
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: url("https://github.com/sushantfreelancer543-bit/BirthdayWeb/blob/main/static/roses.jpg?raw=true");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
h1 {
    color: #ff0066;
    text-shadow: 0 0 20px #ff3399;
}
p {
    font-size: 22px;
    color: white;
    text-shadow: 0 0 10px #00ffff;
}
.symbols {
    font-size: 50px;
    margin-top: 20px;
    animation: glow 2s infinite alternate;
}
@keyframes glow {
    from { text-shadow: 0 0 10px red; }
    to { text-shadow: 0 0 30px yellow; }
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title
st.markdown("<h1>✨ Happy Birthday Akshuu!!! ✨</h1>", unsafe_allow_html=True)

# Message
st.markdown("<p>If the World Was Ending, I'd Wanna be next to you!❤️</p>", unsafe_allow_html=True)

# Symbols
st.markdown('<div class="symbols">❤️ 🌹 ✨ 💎 🔥</div>', unsafe_allow_html=True)

# Music
st.audio("static/birthday_song.mp3", format="audio/mp3", start_time=0)

# Surprise popup (simulate with button)
if st.button("Click for Surprise ❤️"):
    st.success("I Love You Forever ❤️")
