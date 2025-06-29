#to run streamlit use streamlit run app3.py
import streamlit as st
import random

def build_markov_chain(text, n=2):
    words = text.split()
    markov_chain = {}
    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        next_word = words[i + n]
        markov_chain.setdefault(key, []).append(next_word)
    return markov_chain, words  # Also return original word list

def generate_text(chain, words, length=100, n=2):
    # Start from the first n words of the input
    key = tuple(words[:n])
    output = list(key)

    for _ in range(length):
        next_words = chain.get(key)
        if not next_words:
            break
        next_word = random.choice(next_words)
        output.append(next_word)
        key = tuple(output[-n:])  # Update key with latest n words

    return ' '.join(output)

# Streamlit UI
st.title("🧠 Markov Chain Text Generator")

uploaded_file = st.file_uploader("Upload a .txt file", type="txt")

if uploaded_file:
    input_text = uploaded_file.read().decode("utf-8")
    n = st.slider("Select chain depth (n)", 1, 5, 2)
    length = st.slider("Generated text length", 10, 500, 100)

    if st.button("Generate"):
        chain, words = build_markov_chain(input_text, n)
        result = generate_text(chain, words, length, n)
        st.markdown("### ✨ Generated Text")
        st.write(result)
