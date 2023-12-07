from lemmatize import lemmatize_text
import pandas as pd
from yaspin import yaspin
from user_interaction import what_to_do, startup_what_to_do

start_choice = startup_what_to_do()
language = 'fr' # eventually this will be something that is fed to all the functions in the app that would change based on language

def perform_activity(activity_name, first_time=False):
    if activity_name == 'mark knowns':
        from user_interaction import ask_if_words_are_known
        user_choices = ask_if_words_are_known(df['lemma'].tolist())
        df['known'] = user_choices
        df.to_csv('user_data.csv', index=False)
        print('💾 Saved to user_data.csv')
    elif activity_name == 'quiz':
    # get translations - takes way too long with Wiktionary parsing, but could do asynchronously
        from translations_from_wiktionary import get_translations
        translations = df['translations'].tolist()
        with yaspin(text="🔍Getting translations", color="yellow", timer=True) as spinner:
        # go through df, if there's no translation, get it
            for i in range(len(translations)):
                if translations[i] == None:
                    translations[i] = get_translations(df['lemma'][i], language) 
            spinner.ok("✅ Completed")
        
        df['translations'] = translations
        df.to_csv('user_data.csv', index=False)
        print('💾 Saved translations to user_data.csv')
        print('📝 Beggining quiz')
        from user_interaction import quiz_on_words
        unknown_words_indices = df[df['known'] == False].index.tolist()
        unknown_words = df[df['known'] == False]['lemma'].tolist()
        translations = df[df['known'] == False]['translations'].tolist()
        quiz_output = quiz_on_words(unknown_words, translations, first_time=first_time)
        # update df with quiz results
        df.loc[df['lemma'].isin(unknown_words), ['known']] = quiz_output
        df.to_csv('user_data.csv', index=False)
        print('💾 Saved quiz results to user_data.csv')

if start_choice == 'lemmatize new text':
    f = open('petit-prince/chapitre-0.txt', 'r', encoding='utf-8')
    raw = f.read().replace('\n\n','\n').replace('\n', ' ')
    with yaspin(text="Lemmatizing", color="yellow", timer=True) as spinner:
        df = lemmatize_text(raw, 'fr')
    spinner.ok("✅ Completed")
    # save the df to a csv
    df['translations'] = None
    df['known'] = False
    df.to_csv('user_data.csv', index=False)
    print('💾 Saved lemmatized text to user_data.csv')
    # summary statistics - move this to its own file, expand on it
    def first_time_summary_statistics(df):
        output = 'Summary Statistics\n'
        output += '==================\n'
        output += 'Unique lemmas:\n'
        output += str(len(df))
        output += '\nTotal number of words:\n'
        output += str(sum(df['freq']))
        output += '\n==================\n'
        output += 'Most common lemmas:\n'
        output += df.sort_values(by='freq', ascending=False).head(5).to_string(index=False)
        output += '\n==================\n'
        output += 'Least common lemmas:\n'
        output += df.sort_values(by='freq', ascending=True).head(5).to_string(index=False)
        output += '\n=================='
        return output    
    # ask the user what they would like to do
    task = what_to_do(first_time_summary_statistics(df))
    perform_activity(task, first_time=True)

elif start_choice == 'return to saved text':
    df = pd.read_csv('user_data.csv')
    def info_on_return(df):
        output = 'Summary Statistics\n'
        output += '==================\n'
        output += 'Known lemmas:\n'
        output += str(len(df[df['known'] == True]))+' / '+str(len(df)) + ' (' + str(round(len(df[df['known'] == True])/len(df)*100, 1)) + '%)'
        output += '\nKnown words in text:\n'
        output += str(df['freq'][df['known'] == True].sum())+' / '+str(df['freq'].sum()) + ' (' + str(round(df['freq'][df['known'] == True].sum()/df['freq'].sum()*100, 1)) + '%)'
        output += '\n==================\n'
        output += 'Unkown lemmas with most occurences:\n'
        output += df[df['known'] == False].sort_values(by='freq', ascending=False).head(10)[['lemma', 'freq']].to_string(index=False)
        output += '\n==================\n'
        output += 'Unkown lemmas with least occurences:\n'
        output += df[df['known'] == False].sort_values(by='freq', ascending=True).head(5)[['lemma', 'freq']].to_string(index=False)
        output += '\n=================='
        return output
    task = what_to_do(info_on_return(df))
    perform_activity(task)

