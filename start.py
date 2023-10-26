# https://spacy.io/
# start with French. PP vocab from https://gutenberg.net.au/ebooks03/0300771h.html

"""
python3 -m venv venv
source venv/bin/activate
python -m spacy download fr_core_news_sm
"""
import pandas as pd
import spacy 
import tkinter as tk
nlp = spacy.load("fr_core_news_sm")

# read file chapitre-0.txt to a string
f = open('petit-prince/chapitre-0.txt', 'r')
raw = f.read().replace('\n', ' ')

# Process the text with SpaCy
doc = nlp(raw)
words = [token for token in doc if not token.is_punct] # and not token.is_stop takes out stop words: https://github.com/explosion/spaCy/blob/master/spacy/lang/fr/stop_words.py
lemmas = [token.lemma_ for token in words]

# frequency of unique words and unique words to a df
from collections import Counter
word_freq = Counter(lemmas)
common_words = word_freq.most_common(100)
df = pd.DataFrame(common_words, columns = ['words', 'count'])

strings = df['words'].tolist()
current_word_index = 0
user_choices = []

def on_button_click(choice):
    global current_word_index
    user_choices.append(choice)
    current_word_index += 1
    if current_word_index < len(strings):
        label.config(text=f'Do you know the word:\n{strings[current_word_index]}')
    else: 
        root.destroy()
    
root = tk.Tk()
root.title("Vocab Test")

label = tk.Label(root, text=f'Do you know the meaning of the word:\n\n{strings[current_word_index]}\n')
label.pack()

button1 = tk.Button(root, text="Yes", command=lambda: on_button_click(True))
button1.pack()
button2 = tk.Button(root, text="No", command=lambda: on_button_click(False))
button2.pack()

root.mainloop()

df['known'] = user_choices
print(df.head(10))