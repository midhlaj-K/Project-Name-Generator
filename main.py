import streamlit as st
import random

st.markdown("Oh, You Started A New Project? Well Let's Fix A Name For It.")

word_banks = {
    "Adjectives": ["Quantum", "Turbo", "Hyper", "Cursed", "Fuzzy", "Glitchy", "Invisible", "Magic"],
    "Tech": ["Bot", "LLM", "Prompt", "Neuron", "Blockchain", "API", "Kernel", "Script"],
    "Animals": ["Panther", "Llama", "Falcon", "Sloth", "Pigeon", "Cobra", "Whale"],
    "Food": ["Samosa", "Mango", "Pickle", "Noodle", "Tofu", "Biryani", "Dumpling"],
    "Funny Things": ["Toaster", "Blob", "Sock", "Trashcan", "Laserbeam", "Spoon", "Cactus"],
    "AI":["Neural", "Gen", "Predict", "Agent", "Model", "Tensor", "Intelligent", "Adaptive"],
    "Academic":["Book", "Note", "Nerd", "Smart", "Topper", "Textbook", "Tutor", "Tution"],
    "Creative":["Vision", "Dream", "Novel", "New", "Wonder", "Aesthetic", "Fun", "Invent"],
}

st.title("🚀 Project Name Generator")

st.markdown("Choose two word types to create a random project name.")
st.subheader("Let's Start.")
category1 = st.selectbox("First Word Type", list(word_banks.keys()), index=0)
category2 = st.selectbox("Second Word Type", list(word_banks.keys()), index=1)

if st.button("Generate Name 🎉"):
    word1 = random.choice(word_banks[category1])
    word2 = random.choice(word_banks[category2])
    st.subheader(f"**🧠 Your Project Name:**")
    st.success(f"**{word1} {word2}**")

st.markdown("---")
