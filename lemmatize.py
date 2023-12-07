import pandas as pd
from collections import Counter
# use NLTK if ever doing English
import stanza
import string

def lemmatize_text(text, language='fr'):
    """
    Takes in a string of text and returns a df with lemmas and their frequencies 
    """
    nlp = stanza.Pipeline(lang=language, processors='tokenize,mwt,pos,lemma')
    doc = nlp(text)
    lemmas = [word.lemma for sent in doc.sentences for word in sent.words if word.lemma not in string.punctuation]

    lemmas_and_freq = dict(Counter(lemmas))
    df = pd.DataFrame({'lemma': list(lemmas_and_freq.keys()), 'freq': list(lemmas_and_freq.values())})
    df['translations'] = ''

    # save the df to a csv
    df.to_csv('user_data.csv', index=False)
    return df

if __name__ == '__main__':
    # print(lemmatize_text('Bonjour, je m\'appelle John. Je suis un homme.'))

    test_text = """Je demande pardon aux enfants d'avoir dédié ce livre à une grande personne. J'ai une excuse sérieuse : cette grande personne est le meilleur ami que j'ai au monde. J'ai une autre excuse : cette grande personne peut tout comprendre, même les livres pour enfants. J'ai une troisième excuse : cette grande personne habite la France où elle a faim et froid. Elle a besoin d'être consolée. Si toutes ces excuses ne suffisent pas, je veux bien dédier ce livre à l'enfant qu'a été autrefois cette grande personne. Toutes les grandes personnes ont d'abord été des enfants. (Mais peu d'entre elles s'en souviennent.) Je corrige donc ma dédicace."""
    with open('lemmatized_text.txt', 'w') as f:
        f.write(str(lemmatize_text(test_text)))