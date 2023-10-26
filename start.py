# https://spacy.io/
# https://github.com/Suyash458/WiktionaryParser

# Wiktionary scrapper (https://github.com/Suyash458/WiktionaryParser)? Perseus?
# start with French. PP vocab from https://gutenberg.net.au/ebooks03/0300771h.html

"""
python3 -m venv venv
source venv/bin/activate
python -m spacy download fr_core_news_sm
"""
import pandas as pd
import spacy 
nlp = spacy.load("fr_core_news_sm")

# read file chapitre-0.txt to a string
f = open('petit-prince/chapitre-0.txt', 'r')
raw = f.read().replace('\n', ' ')
print(raw[:50])
# Process the text with SpaCy
doc = nlp(raw)
words = [token for token in doc if not token.is_punct] # and not token.is_stop would take out stop words: https://github.com/explosion/spaCy/blob/master/spacy/lang/fr/stop_words.py
lemmas = [token.lemma_ for token in words]

# frequency of unique words and unique words to a df
from collections import Counter
word_freq = Counter(lemmas)
common_words = word_freq.most_common(100)
df = pd.DataFrame(common_words, columns = ['words', 'count'])

df['known'] = 0
for word in range(len(df)):
    print('word: ', df['words'][word],'\noccurences: ', df['count'][word])
    known = input("Do you know this word? (y/n)")
    if known == 'y':
        df['known'][word] = 1
    else:
        df['known'][word] = 0

print(df)