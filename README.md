# learn-corpus
Given a text, learn the vocabulary in it

https://spacy.io/
PP vocab from https://gutenberg.net.au/ebooks03/0300771h.html

app to learn the vocabulary in a text. Given a text, finds all the lemmas (Wiktionary scrapper (https://github.com/Suyash458/WiktionaryParser)? Perseus? other tools Gogglable like https://outils.biblissima.fr/en/eulexis/index.php), lists most common words, and can quiz user on the vocab. It can let the user pick if they want to be quizzed on the ones they got right, or just the ones they haven't. Maybe have it work with English too (takes a long text and gives the least common words)
- maybe learn a little about making UIs for this one
- https://vocabhunter.github.io/help/ https://github.com/VocabHunter/VocabHunter


# every venv on Linux:

python3 -m venv venv
source venv/bin/activate
python -m spacy download fr_core_news_sm