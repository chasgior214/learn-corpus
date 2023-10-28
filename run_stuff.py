from lemmatize import lemmatize_text
# setup - language, get text, lemmatize
language = 'fr' # eventually this will be something that is fed to all the functions in the app that would change based on language
f = open('petit-prince/chapitre-0.txt', 'r', encoding='utf-8')
raw = f.read().replace('\n\n','\n').replace('\n', ' ')
df = lemmatize_text(raw, 'fr')

# maybe make it more like a proper app that starts up when the script starts, it says the progress of processing the text, then it asks the user what they want to do, provides them information, and keeps going until the user quits the app

# summary statistics - move this to its own file, expand on it, remove the indexes from the printed df
def summary_statistics(df):
    output = ''
    output += 'Most common lemmas:\n'
    output += str(df.sort_values(by='freq', ascending=False).head(5))
    output += '\nLeast common lemmas:\n'
    output += str(df.sort_values(by='freq', ascending=True).head(5))
    output += '\nUnique lemmas:\n'
    output += str(len(df))
    output += '\nTotal number of words:\n'
    output += str(sum(df['freq']))
    return output


# ask the user what they would like to do
from user_interaction import what_to_do
task = what_to_do(summary_statistics(df))
print(task)

if task == 'mark knowns':
    from user_interaction import ask_if_words_are_known
    user_choices = ask_if_words_are_known(df['lemma'].tolist())
    df['known'] = user_choices
    print(df)

# translations take way too long with Wiktionary parsing
# get translations 
# from translations_from_wiktionary import get_translations
# translations = []
# for word in df['lemma'].tolist():
#     translations.append(get_translations(word, language))

# from user_interaction import quiz_on_words
# user_choices = quiz_on_words(df['lemma'].tolist(), translations)
# df['known'] = user_choices
# print(df)