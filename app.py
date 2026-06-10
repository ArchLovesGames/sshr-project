import random
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).parent
AFFIRMATIONS_FILE = BASE_DIR / "data" / "affirmations.txt"
IMAGE_FILE = BASE_DIR / "assets" / "thumbs_up.jpeg"


def load_affirmations() -> list[str]:
    if not AFFIRMATIONS_FILE.exists():
        return ["You are doing okay today."]

    return [
        line.strip()
        for line in AFFIRMATIONS_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


st.set_page_config(
    page_title="Daily Affirmations",
    page_icon="🌱",
    layout="centered",
)

st.title("Daily Affirmations")
st.write("A simple Streamlit app that shows a positive message for the day.")

if IMAGE_FILE.exists():
    st.image(str(IMAGE_FILE), use_container_width=True)
else:
    st.info("Add an image at assets/thumbs_up.jpeg to show it here.")

affirmations = load_affirmations()

if "affirmation" not in st.session_state:
    st.session_state.affirmation = random.choice(affirmations)

if st.button("Show another affirmation"):
    st.session_state.affirmation = random.choice(affirmations)

st.subheader(st.session_state.affirmation)
