import random

def build_markov_chain(text, n=2):
    words = text.split()
    index = n
    markov_chain = {}

    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        next_word = words[i + n]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_word)

    return markov_chain


def generate_text(chain, length=100):
    words = []
    # Start from the beginning of the original input
    key = next(iter(chain))  # or use: key = (words[0], words[1])
    words.extend(key)

    for _ in range(length):
        next_words = chain.get(key)
        if not next_words:
            break
        next_word = random.choice(next_words)
        words.append(next_word)
        key = (key[1], next_word)

    return ' '.join(words)


# 📝 Sample Usage
if __name__ == "__main__":
    with open("sample_text.txt", "r", encoding="utf-8") as f:
        input_text = f.read()

    chain = build_markov_chain(input_text)
    new_text = generate_text(chain, length=100)
    print("Generated Text:\n", new_text)
