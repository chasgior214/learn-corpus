import pandas as pd
from collections import Counter
import spacy


def lemmatize_text(text, language='fr'):
    """
    Takes in a string of text and returns a df with lemmas and their frequencies 
    """
    if language == 'fr':
        nlp = spacy.load('fr_core_news_sm')
    elif language == 'en':
        nlp = spacy.load('en_core_web_sm')
    elif language == 'el':
        nlp = spacy.load('el_core_news_sm')

    doc = nlp(text)
    words = [token for token in doc if not token.is_punct] # and not token.is_stop takes out stop words
    lemmas = [token.lemma_ for token in words]

    lemmas_and_freq = dict(Counter(lemmas))
    df = pd.DataFrame({'lemma': list(lemmas_and_freq.keys()), 'freq': list(lemmas_and_freq.values())})
    return df

if __name__ == '__main__':
    print(lemmatize_text('Bonjour, je m\'appelle John. Je suis un homme.'))